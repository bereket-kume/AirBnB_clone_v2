#!/usr/bin/python3
"""display “C ” followed by the value of the text variable """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slahses=False)
def display_hello():
    """display honly hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route():
    """c route appp"""
    text = text.replace('_', ' ')
    return f'C text'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
