#!/usr/bin/python3
"""
flask web application displaying states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Html page that shows a list of States and cities
    sorted alphabetically
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exceptiion):
    """
    deletes current SQLAlchemy sesh
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
