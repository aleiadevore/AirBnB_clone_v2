#!/usr/bin/python3
""" Starts flask application for /, /hbnb, /c/, and /python/ """

from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
        """ Prints Hello HBNB! """
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """ Prints HBNB """
        return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
        """ Prints C followed by input, with underscores as spaces """
        return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
def py_is_fun(text='is fun'):
        """ Prints python followed by input, with underscores as spaces """
        return 'Python %s' % text.replace('_', ' ')


@app.route('/number_template/<n>', strict_slashes=False)
def is_number_temp(n):
        """ displays template if n is a number """
        try:
                a = int(n)
                return render_template('5-number.html', n=n)
        except:
                abort(404)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
