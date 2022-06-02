#!/usr/bin/env python3
import flask
from pathlib import Path
from get_tab import search_bar
import database

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('main.html')

@app.route('/tab')
def tab():
    return flask.render_template('tab.html')

@app.route('/search')
def search():
    division = flask.request.args.get('division')
    search = flask.request.args.get('search')
    search_bar([division, search])
    return flask.render_template('search.html')

@app.route('/getdata')
def get_data():
    return flask.render_template('getdata.html')

@app.route("/main")
def main():
    return flask.render_template("main.html")

@app.route("/contact")
def contact():
    return flask.render_template("contact.html")

@app.route("/cookie")
def cookie():
    return flask.render_template("cookie.html")

@app.route("/log-in")
def login():
    return flask.render_template("log-in.html")

@app.route("/map")
def map():
    return flask.render_template("map.html")

@app.route("/privacy")
def privacy():
    return flask.render_template("privacy.html")

@app.route("/register")
def register():
    return flask.render_template("register.html")

@app.route("/registered")
def registered():
    email = flask.request.args.get('email')
    password = flask.request.args.get('password')
    database.register(email, password)
    return flask.render_template("/")

@app.route("/suppliers")
def suppliers():
    return flask.render_template("searching.html")

@app.route("/searching")
def searching():
    return flask.render_template("suppliers.html")


app.run("127.0.0.1", 3945, debug=True)
