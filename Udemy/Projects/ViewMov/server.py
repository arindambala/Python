# Day 64 - 100 Days of Code

import os
from pathlib import Path
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

SECRET_KEY = os.getenv('SECRET_KEY', "secret-key-change")
DB_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

TMDB_SEARCH_URL = os.getenv('TMDB_SEARCH_URL')
TMDB_INFO_URL = os.getenv('TMDB_INFO_URL')
TMDB_IMAGE_URL = os.getenv('TMDB_IMAGE_URL')

print(f'\n---- Book ^ Archive ----\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Done')

class FindMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add')

@app.route('/')
def home():
    query = db.session.execute(
        db.select(Movie).order_by(Movie.rating.desc())
    )
    movies = query.scalars().all()
    
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    
    return render_template('index.html', movies=movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        
        return redirect(url_for('home'))
    
    if request.method == 'GET':
        form.rating.data = movie.rating
        form.review.data = movie.review

    return render_template('edit.html', movie=movie, form=form)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = FindMovieForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            TMDB_SEARCH_URL,
            params={
                'api_key': TMDB_API_KEY,
                'query': movie_title
            }
        )
        data = response.json()
        
        return render_template('select.html', options=data)
    
    return render_template('add.html', form=form)

@app.route('/search')
def search():
    movie_api_id = request.args.get('id')
    
    if movie_api_id:
        movie_url = f'{TMDB_INFO_URL}/{movie_api_id}'
        response = requests.get(
            movie_url,
            params={
                'api_key': TMDB_API_KEY
            }
        )
        data = response.json()
        
        new_movie = Movie(
            title = data['title'],
            year = data['release_date'].split('-')[0],
            description = data['overview'],
            rating = 0.0,
            ranking = 0,
            review = 'No review yet!',
            img_url = f"{TMDB_IMAGE_URL}{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        
        return redirect(url_for('edit', id=new_movie.id))

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    
    db.session.delete(movie_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)