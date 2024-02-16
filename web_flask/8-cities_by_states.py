#!/usr/bin/python3
"""This script starts a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exec):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
