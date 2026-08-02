# Day 67 - 100 Days of Code

import os 
from pathlib import Path
from dotenv import load_dotenv
from datetime import date
from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user, logout_user
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import hashlib

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

SECRET_KEY = os.getenv('SECRET_KEY')
DB_URL = os.getenv('SQLALCHEMY_DATABASE_URI')

print(f'\n---- Blog ^ Site ----\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, int(user_id))

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    
    return decorated_function

def gravatar_url(email, size=100, rating='g', default='retro'):
    hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    
    return f'https://www.gravatar.com/avatar/{hash}?s={size}&d={default}&r={rating}'

app.jinja_env.globals.update(gravatar_url=gravatar_url)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    
    posts = relationship('BlogPost', back_populates='author')
    comments = relationship('Comment', back_populates='comment_author')

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
    comments = relationship('Comment', back_populates='parent_post')

class Comment(db.Model):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    comment_author = relationship('User', back_populates='comments')
    
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('blog_posts.id'))
    parent_post = relationship('BlogPost', back_populates='comments')

with app.app_context():
    db.create_all()

class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Sign me up!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log me in!')

class CommentForm(FlaskForm):
    comment_text = CKEditorField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Comment')

@app.route('/')
def home():
    query = db.session.execute(db.select(BlogPost))
    posts = query.scalars().all()
    
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
@login_required
@admin_only
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            body = form.body.data,
            img_url = form.img_url.data,
            author = current_user,
            date = date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('create.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        query = db.session.execute(db.select(User).where(User.email == form.email.data))
        user_exists = query.scalar()
        
        if user_exists:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('register'))
        
        hash_salt = generate_password_hash(
            form.password.data,
            method = 'pbkdf2:sha256',
            salt_length=8
        )
        
        new_user = User(
            email = form.email.data,
            name = form.name.data,
            password = hash_salt
        )
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        
        return redirect(url_for('home'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        query = db.session.execute(db.select(User).where(User.email == email))
        user = query.scalar()
        
        if not user:
            flash('Email does not exist! Please try again.')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect! Please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
            
    return render_template('login.html', form=form)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    query_post = db.get_or_404(BlogPost, post_id)
    
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Need to login or register to comment! Please try again.')
            return redirect(url_for('login'))
        
        new_comment = Comment(
            text = form.comment_text.data,
            comment_author = current_user,
            parent_post = query_post
        )
        db.session.add(new_comment)
        db.session.commit()
        
        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template('post.html', post=query_post, form=form)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
@admin_only
def edit(post_id):
    query_edit = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title = query_edit.title,
        subtitle = query_edit.subtitle,
        img_url = query_edit.img_url,
        body = query_edit.body
    )
    
    if edit_form.validate_on_submit():
        query_edit.title = edit_form.title.data
        query_edit.subtitle = edit_form.subtitle.data
        query_edit.img_url = edit_form.img_url.data
        query_edit.body = edit_form.body.data
        
        db.session.commit()
        
        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template('create.html', form=edit_form, is_edit=True)

@app.route('/delete/<int:post_id>')
@login_required
@admin_only
def delete(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    
    db.session.delete(post_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)