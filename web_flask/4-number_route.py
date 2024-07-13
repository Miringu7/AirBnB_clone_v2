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


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """
    Replaces _ with space
    Returns:
    value of text
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """returns Python followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns n is a number"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    """
    Running the Flask application
    """
    app.run(host='0.0.0.0', port=5000)