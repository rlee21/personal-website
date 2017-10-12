#!venv/bin/python3.6

import os
from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/resume.pdf')
def resume():
    file_path = './static/doc/resume.pdf'
    return send_file(file_path, attachment_filename='resume.pdf')


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
