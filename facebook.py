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

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/posts/new', method=['POST'])
def newPosts():

    if request.method == 'POST':
        strText = request.form['text']

    return redirect(url_for('posts'))

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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['password']
        password = request.form['password']
        
        user_id = getUserID(email)
        if not user_id:
            redirect(url_for('login'))

        login_session['userid'] = user_id
        
        return redirect(url_for('homepage'))
    else:
        return render_template('login.html')

    return redirect(url_for('homepage'))

@app.route('/logout', methods=['POST'])
def logout():
    del login_session['userid']
    
    return redirect(url_for('homepage'))

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8000, debug=True)