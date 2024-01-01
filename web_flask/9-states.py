#!/usr/bin/python3
"""
A Python script that starts a flask web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Display a HTML page
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Display a HTML page
    """
    return render_template("9-states.html", states=storage.all(State).get
                          ("State.{}".format(id)))


@app.teardown_appcontext
def session_close(exception):
    """
    A method to remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
