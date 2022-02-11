from db import db
from flask import session

def workout(user_id, workout):
    workoutNumber = latest_workout(user_id) + 1 or 1
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

    if squatsets:
        for i in range(1,squatsets + 1):
            for key in workout:
                if str(i) + "squatset" in key:
                    if "weight" in key:
                        weight = float(workout[key])
                    if "sets" in key:
                        sets = int(workout[key])
                    if "reps" in key:
                        reps = int(workout[key])
            sql = "INSERT INTO squatsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
            db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
            db.session.commit()

    if deadliftsets:
        for i in range(1,deadliftsets + 1):
            for key in workout:
                if str(i) + "deadliftset" in key:
                    if "weight" in key:
                        weight = float(workout[key])
                    if "sets" in key:
                        sets = int(workout[key])
                    if "reps" in key:
                        reps = int(workout[key])
            sql = "INSERT INTO deadliftsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
            db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
            db.session.commit()
        
def latest_workout(user_id):
    return db.session.execute("SELECT MAX(workout_id) FROM userworkouts WHERE user_id=:id", {"id":user_id}).fetchone().max

def user_history(user_id):
    return db.session.execute("SELECT workout_id FROM userworkouts WHERE user_id=:id", {"id":user_id}).fetchall()

def bench_view(workout_id, user_id):
    return db.session.execute("SELECT weight, sets, reps FROM benchsets WHERE workout_id=:wid AND user_id=:uid", {"wid":workout_id, "uid":user_id}).fetchall()
def squat_view(workout_id, user_id):
    return db.session.execute("SELECT weight, sets, reps FROM squatsets WHERE workout_id=:wid AND user_id=:uid", {"wid":workout_id, "uid":user_id}).fetchall()
def deadlift_view(workout_id, user_id):
    return db.session.execute("SELECT weight, sets, reps FROM deadliftsets WHERE workout_id=:wid AND user_id=:uid", {"wid":workout_id, "uid":user_id}).fetchall()

def maxlifts(user_id):
    #WIP
    return db.session.execute("SELECT * FROM maxlifts WHERE user_id=:id", {"id":user_id}).fetchall()