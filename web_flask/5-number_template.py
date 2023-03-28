#!/usr/bin/python3
"""
Task 3: script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_n(n):
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)