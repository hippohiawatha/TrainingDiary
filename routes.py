from flask.helpers import url_for
from app import app
from db import db
from flask import redirect, render_template, request, session
import users
import workouthandlers

@app.route("/")
@app.route("/home")
def home():
    return redirect("welcome")

@app.route("/maxlifts")
def maxlifts():
    #WIP
    if session["id"]:
        data = workouthandlers.maxlifts(session["id"])
        if data:
            return render_template("maxlifts.html", data=data)
    return render_template("maxlifts.html", data = "You haven't maxed out yet!")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        loggedIn = users.login(username, password)
        if(loggedIn == True):
            return redirect("welcome")
        elif(loggedIn == "name"):
            return render_template("login.html", failed = "name")   
        elif(loggedIn == "password"):
            return render_template("login.html", failed = "pw")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        loggedIn = users.register(username, password)
        
        if(loggedIn):
            return redirect("/")
        else:
            return redirect("/", issue = loggedIn)
    else:
        return render_template("register.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/workout_input", methods=["GET", "POST"])
def workout():
    if not session["username"]:
        return redirect("/")

    username = session["username"]
    user_id = session["id"]
    workoutNumber = workouthandlers.latest_workout(user_id) + 1 or 1

    if request.method == "POST":
        workouthandlers.workout(user_id, request.form)
        return redirect(url_for("workout_view", wid = workoutNumber))

    return render_template("workout_input.html", workoutNo = workoutNumber)

@app.route("/user_history")
def user_history():
    if not session["username"] or not session["id"]:
        return redirect("/")

    workouts = workouthandlers.user_history(session["id"])
    return render_template("user_history.html", data = workouts)

@app.route("/workout_view/<int:wid>")
def workout_view(wid):
    if not session["username"] or not session["id"] or not wid:
        return redirect("/")

    benches = workouthandlers.bench_view(wid, session["id"])
    squats = workouthandlers.squat_view(wid, session["id"])
    deadlifts = workouthandlers.deadlift_view(wid, session["id"])
    name = workouthandlers.workoutName(session["id"], wid)

    return render_template("views/workout_view.html", benchsets = benches, squatsets = squats, deadliftsets = deadlifts, workoutName = name, wid=wid)

