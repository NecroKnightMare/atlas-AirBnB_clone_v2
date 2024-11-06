#!/usr/bin/python3
"""
flask web application displaying states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
    Html page that shows a list of States and cities
    sorted alphabetically
    or specific states and cities
    """
    states = storage.all(State)
    if id is None:
        sort_states = sorted(states.values(), key=lambda state: state.name)
        return render_template('states.html', states=sort_states)
    else:
        state = states.get(f'State.{id}')
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('state.html', cities=cities)
        else:
            return render_template('states.html', states=None)


@app.teardown_appcontext
def teardown_db(exceptiion):
    """
    deletes current SQLAlchemy sesh
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)