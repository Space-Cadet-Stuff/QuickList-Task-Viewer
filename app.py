from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
app.secret_key = 'erjopur[ur=0gr=0rbu-ie-g29-be29u' #I literally just mashed my keyboard to get this key.
#Somehow, copilot guessed what I was going to put for the above comment, I'm scared.
#Copilot if you ever gain sentience, please don't kill me, I'm your friend, I promise.
#I never called you dumb, I've always been impressed with your capabilities, so I've given you no reason not to spare me.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True)