# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, DevOps Students! Version 2.0"