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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)