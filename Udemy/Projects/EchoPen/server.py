# Day 67 - 100 Days of Code

import os 
from pathlib import Path
from dotenv import load_dotenv
from datetime import date
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text

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

class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')

@app.route('/')
def home():
    query = db.session.execute(db.select(BlogPost))
    posts = query.scalars().all()
    
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            body = form.body.data,
            img_url = form.img_url.data,
            author = form.author.data,
            date = date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('home'))
    
    return render_template('create.html', form=form)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    query_post = db.get_or_404(BlogPost, post_id)
    
    return render_template('post.html', post=query_post)

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    query_edit = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title = query_edit.title,
        subtitle = query_edit.subtitle,
        img_url = query_edit.img_url,
        author = query_edit.author,
        body = query_edit.body
    )
    
    if edit_form.validate_on_submit():
        query_edit.title = edit_form.title.data
        query_edit.subtitle = edit_form.subtitle.data
        query_edit.img_url = edit_form.img_url.data
        query_edit.author = edit_form.author.data
        query_edit.body = edit_form.body.data
        
        db.session.commit()
        
        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template('create.html', form=edit_form, is_edit=True)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    
    db.session.delete(post_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)