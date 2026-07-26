# Day 62 - 100 Days of Code

from flask import Flask, render_template

print(f'\n---- Coffee ^ WiFi ----\n')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)