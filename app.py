from flask import Flask, render_template, request, session, redirect, url_for, flash
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from setup_db import User, ToDo

app = Flask(__name__)
app.secret_key = 'erjopur[ur=0gr=0rbu-ie-g29-be29u'

engine = create_engine('sqlite:///todo.db')
Session = sessionmaker(bind=engine)
db_session = Session()

# Define the index route
@app.route('/')
def index():
    return render_template('index.html')# Renders the index page

# Define the login route, same as the index
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":# Takes the username and password data from the login
        username = request.form.get('username')
        password = request.form.get('password')

        user = db_session.query(User).filter_by(username=username).first()# Checks if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Logged in successfully", "info")
            return redirect(url_for('dashboard'))# Logs in the user and redirects to the dashboard
        else:
            flash("Invalid username or password", "error")# If the user does not exist or the password is incorrect, it flashes an error message

    return render_template('login.html')# Renders the login page

# Define the signup route
@app.route('/signup')
def signup():
    return render_template('signup.html')# Renders the signup page

# Define the homepage route
@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:# Checks if the user is logged in, and redirects to login if not
        flash("You need to login first", "warning")
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user_id=session["user_id"], username=session["username"])# Renders the dashboard page and stores the current users id and username in the session

# Define the create route
@app.route('/create')
def create():
    if "user_id" not in session:# Checks if the user is logged in, and redirects to login if not
        flash("You need to login first", "warning")
        return redirect(url_for('login'))

    return render_template('create.html', user_id=session["user_id"], username=session["username"])# Renders the create page and stores the current users id and username in the session

# Defines the logout route
@app.route('/logout')
def logout():
    session.clear()# Clears the session
    flash("You have been logged out", "info")
    return redirect(url_for('index'))# Redirects to the index page

app.run(debug=True)# Runs the app in debug mode