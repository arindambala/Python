# Day 57 - 100 Days of Code

import os
import requests
from flask import Flask, render_template
import random
from datetime import datetime
from dotenv import load_dotenv
from post import Post

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

GENDER = os.getenv('GENDER_URL')
AGE = os.getenv('AGE_URL')
BLOG = os.getenv('BLOG_URL')

print('\n---- Jinja ^ Templates ----\n')

blogs = requests.get(BLOG)
blogs.raise_for_status()

blogs_data = blogs.json()

blog_objects = []
for blog in blogs_data:
    blog_obj = Post(blog['id'], blog['title'], blog['subtitle'], blog['body'])
    blog_objects.append(blog_obj)

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0, 9)
    curr_year = datetime.now().year
    return render_template('index.html', num=random_number, foot=curr_year)

@app.route('/guess/<name>')
def stat(name):
    payload = {'name': name}
    
    gender_response = requests.get(GENDER, params=payload).json()
    age_response = requests.get(AGE, params=payload).json()
    
    gender_stat = gender_response.get('gender', 'unknown')
    age_stat = age_response.get('age', 'unknown')
    
    return render_template('site.html', name=name, gender=gender_stat, age=age_stat)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(BLOG)
    response.raise_for_status()
    
    data = response.json()
    
    return render_template('blog.html', blogs=data)

@app.route('/blogs')
def render_blogs():
    return render_template('_blog.html', blogs=blog_objects)

@app.route('/blogs/post/<int:index>')
def render_posts(index):
    request_post = next((post for post in blog_objects if post.id == index), None)
    return render_template('post.html', post=request_post)

if __name__ == '__main__':
    app.run(debug=True)