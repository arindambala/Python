# Day 56 - 100 Days of Code

import os
from flask import Flask, render_template
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

print('\n---- Static ^ Templates ----\n')

app = Flask(__name__)

GIPHY = os.getenv('WEB')
SITE = os.getenv('TEMPLATE')

@app.route('/')
def home():
    return render_template('site.html', web_link=GIPHY, web_site=SITE)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)