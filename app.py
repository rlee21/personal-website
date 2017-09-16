#!/usr/bin/python

import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
