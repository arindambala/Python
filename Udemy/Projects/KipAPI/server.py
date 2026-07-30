# Day 66 - 100 Days of Code

import os
from pathlib import Path
from dotenv import load_dotenv
import random
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

DB_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
API_KEY = os.getenv('API_KEY')

print(f'\n---- RESTful ^ API ----\n')

app = Flask(__name__)
bootstrap = Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random')
def cafe():
    query = db.session.execute(db.select(Cafe))
    cafe_list = query.scalars().all()
    random_cafe = random.choice(cafe_list)
    
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def cafes():
    query = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    cafe_list = query.scalars().all()
    
    return jsonify(cafes=[cafe.to_dict() for cafe in cafe_list])

@app.route('/search')
def loc():
    query_location = request.args.get('loc')
    
    cafe_loc = db.session.execute(db.select(Cafe).where(Cafe.location.ilike(f'%{query_location}%')))
    cafe_list = cafe_loc.scalars().all()
    
    if not cafe_list:
        return jsonify(error = {
            "Not Found": f"Apologies! We don't have a cafe at that location! ({query_location})"
        }), 404
    
    return jsonify(cafes=[cafe.to_dict() for cafe in cafe_list])

@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(response = {
        "Success": "Successfully added the new cafe!"
    })

@app.route('/update/<int:cafe_id>', methods=['PATCH'])
def update(cafe_id):
    query_price = request.args.get('new_price')
    cafe = db.session.get(Cafe, cafe_id)
    
    if cafe:
        cafe.coffee_price = query_price
        db.session.commit()
        
        return jsonify(response = {
            "Success": "Successfully updated the coffee price!"
        }), 200
    
    else:
        return jsonify(error = {
            "Not Found": "Apologies! We don't have a cafe with that id in the database!"
        }), 404

@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    query_key = request.args.get('api_key')
    cafe = db.session.get(Cafe, cafe_id)
    
    if query_key != API_KEY:
        return jsonify(error = {
            "Forbidden": "Abort! Invalid API key provided!"
        }), 403
    
    else:
        if not cafe:
            return jsonify(response = {
                "Not Found": "Apologies! We don't have a cafe with that id in the database!"
            }), 404
        
        else:
            db.session.delete(cafe)
            db.session.commit()
            
            return jsonify(response = {
                "Success": "Successfully deleted the cafe from the database!"
            }), 200

if __name__ == '__main__':
    app.run(debug=True)