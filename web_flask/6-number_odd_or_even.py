#!/usr/bin/python3
"""
A Python script that starts a flask web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Prompt method for Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Prompt method for HBNB display
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Prompt method for C display
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Prompt method for Python display
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Prompt method for number display
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Prompt method for number_template display
    """
    return render_template("5-number.html", value=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Prompt method for number_odd_or_even display
    """
    return render_template("6-number_odd_or_even.html", value=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
