#!/usr/bin/python3
"""
flask web application displaying states
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Html page that shows a list of States and amenities
    sorted alphabet
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exceptiion):
    """
    deletes current SQLAlchemy sesh
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
