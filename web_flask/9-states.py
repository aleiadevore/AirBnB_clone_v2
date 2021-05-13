#!/usr/bin/python3
""" starts Flask app using db """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
        """ List of cities by state ID """
        all_states = storage.all(State)
        if id == None:
                return render_template(
                        '9-states.html', states=all_states, id=id)
        for instance in all_states.values():
                if instance.id == id:
                        state = instance
        return render_template(
                '9-states.html', states=state, id=id)


@app.teardown_appcontext
def teardown(self):
        """ Removes current session """
        storage.close()

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
