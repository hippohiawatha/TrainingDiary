"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from TrainingDiary import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost:5432/TrainingDiary"
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/maxlifts')
def maxlifts():
    result = db.session.execute("SELECT * FROM maxlifts")
    data = result.fetchall()
    return render_template("maxlifts.html", data = data[0][0])