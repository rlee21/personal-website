#!venv/bin/python3.6

import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
