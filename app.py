"""
Routes and views for the flask application.
"""

from datetime import datetime
import os
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("postgres://", "postgresql://")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    """Renders the home page."""
    return redirect("welcome")
    #return render_template(
    #    "index.html",
    #    title="Home Page",
    #    year=datetime.now().year,
    #)

@app.route("/maxlifts")
def maxlifts():
    result = db.session.execute("SELECT * FROM maxlifts")
    data = result.fetchall()
    return render_template("maxlifts.html", data=data[0][0])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "SELECT id, password FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if not user:
            return render_template("login.html", failed = "name")        
            
        else:
            hash_value = user.password
            if check_password_hash(hash_value, password):
                session["username"] = username
                return redirect("welcome")
            else:
                return render_template("login.html", failed = "pw")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    #TODO: Form username input listener for unique names 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        session["username"] = username
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/workout", methods=["GET", "POST"])
def workout():
    username = session["username"]
    user_id = db.session.execute("SELECT id FROM users WHERE username=:name", {"name":username}).fetchone().id
    workouts = db.session.execute("SELECT MAX(workout_id) FROM userworkouts WHERE user_id=:id", {"id":user_id}).fetchone().max
    workoutNumber = workouts + 1 if workouts else 1

    if request.method == "POST":
        workout = request.form
        benchsets =  int(workout["benchsets"]) if workout["benchsets"] else None
        squatsets =  int(workout["squatsets"]) if workout["squatsets"] else None
        deadliftsets = int(workout["deadliftsets"]) if workout["deadliftsets"] else None
        if benchsets or squatsets or deadliftsets:
            db.session.execute("INSERT INTO userworkouts (user_id, workout_id) VALUES (:uid, :wid)", {"uid":user_id, "wid":workoutNumber})
            db.session.commit()
        if benchsets:
            for i in range(1,benchsets + 1):
                for key in workout:
                    if str(i) + "benchset" in key:
                        if "weight" in key:
                            weight = float(workout[key])
                        if "sets" in key:
                            sets = int(workout[key])
                        if "reps" in key:
                            reps = int(workout[key])
                sql = "INSERT INTO benchsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
                db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
                db.session.commit()
    return render_template("workout.html", workoutNo = workoutNumber)

@app.route("/user_history")
def user_history():
    return render_template("user_history.html")