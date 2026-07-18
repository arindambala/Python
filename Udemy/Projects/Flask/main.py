# Day 54 - 100 Days of Code

from flask import Flask

print(f'\n---- Simple ^ Setup ----\n') # Server

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)