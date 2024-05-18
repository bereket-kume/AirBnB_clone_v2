#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "“Hello HBNB!"


@app.route('/HBNB', strict_slashes=False)
def hbnb():
    return "HBNB"
