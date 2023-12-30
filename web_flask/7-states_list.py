#!/usr/bin/python3
"""
A Python script that starts a flask web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display a HTML page
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def session_close(exception):
    """
    A method to remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
