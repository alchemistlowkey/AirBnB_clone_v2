#!/usr/bin/python3
"""
A Python script that starts a flask web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page
    """
    return render_template("10-hbnb_filters.html", states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def session_close(exception):
    """
    A method to remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
