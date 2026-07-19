# Day 54 - 100 Days of Code

from flask import Flask
import webbrowser

print(f'\n---- Simple ^ Setup ----\n') # Server

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)