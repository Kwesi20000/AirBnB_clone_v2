#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" on the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" on the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    txt = text.replace('_', ' ')
    return "C {}".format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Display "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    txt = text.replace('_', " ")
    return "Python {}".format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer.
    H1 tag: "Number: n" inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer.
    H1 tag: "Number: n is even|odd" inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
