# Day 59 - 100 Days of Code

import os
import requests
from flask import Flask, render_template, url_for
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

BLOG = os.getenv('BLOG_URL')

print('\n---- Blog ^ Website ----\n')

def get_blogs():
    try:
        response = requests.get(BLOG)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, TypeError):
        return []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=get_blogs())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:blog_id>')
def post_blog(blog_id):
    posts = get_blogs()
    post = next((p for p in posts if p.get('id') == blog_id), None)
    if not post:
        return 'Not found post!', 404
    
    if not post.get('image'):
        post['image'] = url_for('static', filename='assets/img/post-bg.jpg')
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)