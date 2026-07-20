# Day 55 - 100 Days of Code

import os
from flask import Flask
from functools import wraps
import random
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

print(f'\n---- URL ^ Parse ----\n')

def make_bold(function):
    @wraps(function)
    def wrapper():
        return f'<b>{(function())}</b>'
    return wrapper

def add_emphasis(function):
    @wraps(function)
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def add_underline(function):
    @wraps(function)
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

IMG_GIF = os.getenv('POKEMON_URL')
NUM_GIF = os.getenv('NUMBER_URL')
HIGH_GIF = os.getenv('UP_IMG_URL')
LOW_GIF = os.getenv('DOWN_IMG_URL')
GUESS_GIF = os.getenv('GUESS_IMG_URL')

@app.route('/konnichiwa')
def moshi_moshi():
    return f'''
            <h1 style="text-align: center">Hello, World!</h1>
            <p>This is a paragraph.</p>
            <img src="{IMG_GIF}" width=200/>
            '''

@app.route('/sayonara')
@make_bold
@add_emphasis
@add_underline
def bubye():
    return 'Matane!'

@app.route('/<name>/<int:number>')
def hello_world(name, number):
    return f'Hello, {name}. Fav number - {number}!'

@app.route('/')
def home():
    return f'''
            <h1>Guess the number : 0 - 9<h1>
            <img src="{NUM_GIF}"/>
            '''

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return f'''
                <h1 style="color: red">Too HIGH. Try again!</h1>
                <img src="{HIGH_GIF}"/>
                '''
    elif guess < random_number:
        return f'''
                <h1 style="color: orange">Too LOW. Think more!</h1>
                <img src="{LOW_GIF}"/>
                '''
    else:
        return f'''
                <h1 style="color: green">Bullseye! Perfect!</h1>
                <img src="{GUESS_GIF}"/>
                '''

if __name__ == '__main__':
    app.run(debug=True)