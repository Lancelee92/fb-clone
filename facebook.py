from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from http.server import BaseHTTPRequestHandler, HTTPServer
from database_setup import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import session as login_session

import httplib2
import json
import requests
import cgi

app = Flask(__name__)

engine = create_engine('postgresql://fb:password@localhost/facebook')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/home/JSON')
def userJSON():
    users = session.query(User)
    return jsonify(users=[r.serialize for r in users])

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/user/new', methods=['POST'])
def newCategory():
    if request.method == 'POST':
        
        fname = request.form['name']
        lname = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        newUser = User(firstname=fname, lastname=lname, email=email, password=password)
        session.add(newUser)
        session.commit()
        return redirect(url_for('userJSON'))

    return redirect(url_for('homepage'))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('homepage'))

    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8000, debug=True)