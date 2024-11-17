from flask import Flask, render_template, request, session, redirect, url_for, flash
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'erjopur[ur=0gr=0rbu-ie-g29-be29u'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = db_session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Logged in successfully", "info")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password", "danger")

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("You need to login first", "warning")
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user_id=session["user_id"], username=session["username"])

@app.route('/create')
def create():
    if "user_id" not in session:
        flash("You need to login first", "warning")
        return redirect(url_for('login'))

    return render_template('create.html', user_id=session["user_id"], username=session["username"])

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", "info")
    return redirect(url_for('index'))

app.run(debug=True)