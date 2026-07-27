# Day 62 - 100 Days of Code

import os
import csv
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

SECRET = os.getenv('SECRET_KEY', "secret-key-change")

print(f'\n---- Coffee ^ WiFi ----\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET
bootstrap = Bootstrap5(app)

CSV_FILE = 'cafe_data.csv'

class CafeForm(FlaskForm):
    cafe = StringField(
        'Cafe Name', 
        validators=[DataRequired(message="Cafe name is required.")]
    )
    location = StringField(
        'Cafe Location on Google Maps (URL)', 
        validators=[
            DataRequired(message="Location URL is required."), 
            URL(message="Please enter a valid URL.")
        ]
    )
    open = StringField(
        'Opening Time (e.g. 8AM)', 
        validators=[DataRequired(message="Opening time is required.")]
    )
    close = StringField(
        'Closing Time (e.g. 5:30PM)', 
        validators=[DataRequired(message="Closing time is required.")]
    )
    coffee_rating = SelectField(
        'Coffee Rating',
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired(message="Please select a coffee rating.")]
    )
    wifi_rating = SelectField(
        'WiFi Strength Rating',
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired(message="Please select a WiFi rating.")]
    )
    power_rating = SelectField(
        'Power Socket Availability',
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired(message="Please select a power rating.")]
    )
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def cafes():
    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',')
        row_list = [row for row in data]
    
    headers = row_list[0] if row_list else []
    cafe_data = row_list[1:] if len(row_list) > 1 else []
    
    return render_template('cafe.html', headers=headers, cafes=cafe_data)

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    
    if form.validate_on_submit():
        with open(CSV_FILE, mode='a', encoding='utf-8', newline='') as file:
            annex = csv.writer(file, lineterminator='\n')
            annex.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data,
            ])
        return redirect(url_for('cafes'))
    
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)