#!/usr/bin/env python3
import flask
from pathlib import Path
from get_tab import search_bar

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/search')
def search():
    division = flask.request.args.get('division')
    search = flask.request.args.get('search')
    search_bar([division, search])
    return flask.render_template('tab.html')

@app.route('/supplier_page')
def suppliers():
    return flask.render_template('supplier_page.html')

@app.route("/main")
def main():
    return flask.render_template("main.html")

app.run("127.0.0.1", 3945, debug=True)