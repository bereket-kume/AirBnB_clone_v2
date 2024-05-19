#!/usr/bin/python3
""" Flask web application that routing """

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def state_list():
    """ display state list in order """
    states = storage.all('State')
    return render_template('7-states_list.html', states - states)


@app.teardown_appcontext
def teardown(exc):
    """ close connection between storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
