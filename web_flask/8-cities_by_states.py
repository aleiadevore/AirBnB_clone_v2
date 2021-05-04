#!/usr/bin/python3
""" starts Flask app using db """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
        """ Displays all State objects """
        all_states = storage.all(State)
        return render_template(
                '8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def teardown(self):
        """ Removes current session """
        storage.close()

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
