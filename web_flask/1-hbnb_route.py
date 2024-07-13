#!/usr/bin/python3
"""Rouuting Hello HBNB"""

from flask import Flask

# Create Flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Hello World

    Returns:
        [String] -- [Hello HBNB!]
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles /hbnb routes
    Returns:
    string "HBNB"
    """
    return 'HBNB'


if __name__ == "__main__":
    """
    Running the Flask application
    """
    app.run(host='0.0.0.0', port=5000)