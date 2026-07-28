# Day 63 - 100 Days of Code

import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

DB_URL = os.getenv('SQLALCHEMY_DATABASE_URI')

class Base(DeclarativeBase):
    pass

print(f'\n---- Structured ^ Queries ----\n')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

with app.app_context():
    existing_book = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    if not existing_book:
        new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)
        db.session.add(new_book)
        db.session.commit()

@app.route('/')
def home():
    return '<h1>My Book Collection Database is Live!</h1>'

if __name__ == '__main__':
    app.run(debug=True)