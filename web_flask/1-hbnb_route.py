#!/usr/bin/python3
""" Starts flask application for /hbnb """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
        """ Prints Hello HBNB! """
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """ Prints HBNB """
        return 'HBNB'

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
