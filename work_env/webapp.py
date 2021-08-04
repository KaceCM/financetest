from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

@app.route('/hi')
def jsp():
    return "who"

@app.route('/hi/<username>')
def greet(username):
    return f"hello, {username}"