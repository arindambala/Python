# Day 61 - 100 Days of Code

import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
    load_dotenv(ENV_FILE)

SECRET = os.getenv('SECRET_KEY', "secret-key-change")
ID = os.getenv('MAIL_ADDRESS')
KEY = os.getenv('PASSWORD')

print(f'\n---- WT ^ Forms ----\n')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField(
        label='Email', 
        validators=[DataRequired(), Email(message='Please enter a valid MAIL ID')]
    )
    password = PasswordField(
        label='Password', 
        validators=[DataRequired(), Length(min=8, message='Password must be 8 characters long')]
    )
    submit = SubmitField(label='Log In')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        
        if email == ID and password == KEY:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)