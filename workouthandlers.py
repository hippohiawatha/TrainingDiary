from db import db
from flask import session

def workout(user_id, workout):
    workoutNumber = latest_workout(user_id) + 1 or 1
    benchsets =  int(workout["benchsets"]) if workout["benchsets"] else None
    squatsets =  int(workout["squatsets"]) if workout["squatsets"] else  None
    deadliftsets = int(workout["deadliftsets"]) if workout["deadliftsets"] else None
    maxl = None
    newMax = False
    benchWeights = []
    squatWeights = []
    deadliftWeights = []

    if benchsets is not None or squatsets is not None or deadliftsets is not None:
        db.session.execute("INSERT INTO userworkouts (user_id, workout_id) VALUES (:uid, :wid)", {"uid":user_id, "wid":workoutNumber})
        db.session.commit()
        maxl = maxlifts(user_id)

    if benchsets is not None:
        for i in range(1,benchsets + 1):
            for key in workout:
                if str(i) + "benchset" in key:
                    if "weight" in key:
                        weight = float(workout[key])
                        benchWeights.append(weight)
                    if "sets" in key:
                        sets = int(workout[key])
                    if "reps" in key:
                        reps = int(workout[key])
            sql = "INSERT INTO benchsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
            db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
            db.session.commit()
        
        newMax = isNewMax(max(benchWeights), maxl.bench or 0) if maxl is not None else True

    if squatsets is not None:
        for i in range(1,squatsets + 1):
            for key in workout:
                if str(i) + "squatset" in key:
                    if "weight" in key:
                        weight = float(workout[key])
                        squatWeights.append(weight)
                    if "sets" in key:
                        sets = int(workout[key])
                    if "reps" in key:
                        reps = int(workout[key])
            sql = "INSERT INTO squatsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
            db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
            db.session.commit()

        newMax = isNewMax(max(squatWeights), maxl.squat or 0) if maxl is not None else True
                
    if deadliftsets is not None:
        for i in range(1,deadliftsets + 1):
            for key in workout:
                if str(i) + "deadliftset" in key:
                    if "weight" in key:
                        weight = float(workout[key])
                        deadliftWeights.append(weight)
                    if "sets" in key:
                        sets = int(workout[key])
                    if "reps" in key:
                        reps = int(workout[key])
            sql = "INSERT INTO deadliftsets (user_id, weight, sets, reps, workout_id) VALUES (:uid, :weight, :sets, :reps, :wid)"
            db.session.execute(sql, {"uid":user_id, "weight":weight, "sets":sets, "reps":reps, "wid":workoutNumber})
            db.session.commit()
        
        newMax = isNewMax(max(deadliftWeights), maxl.deadlift or 0) if maxl is not None else True
         
    if maxl is not None and newMax:
        bmax = max(max(benchWeights), maxl.bench or 0) if len(benchWeights) > 0 else maxl.bench
        smax = max(max(squatWeights), maxl.squat or 0 ) if len(squatWeights) > 0 else maxl.squat
        dlmax = max(max(deadliftWeights), maxl.deadlift or 0) if len(deadliftWeights) > 0 else maxl.deadlift
        sql = "UPDATE maxlifts SET bench=:bmax, squat=:smax, deadlift=:dlmax WHERE user_id=:user_id"
        db.session.execute(sql, {"bmax":bmax, "smax":smax, "dlmax":dlmax, "user_id":user_id})
        db.session.commit()

    elif newMax:
        bmax = max(benchWeights) if len(benchWeights) > 0 else None
        smax = max(squatWeights) if len(squatWeights) > 0 else None
        dlmax = max(deadliftWeights) if len(deadliftWeights) > 0 else None
        sql = "INSERT INTO maxlifts (bench, squat, deadlift, user_id) VALUES (:bmax, :smax, :dlmax, :user_id)"
        db.session.execute(sql, {"bmax":bmax, "smax":smax, "dlmax":dlmax, "user_id":user_id})
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
    return db.session.execute("SELECT * FROM maxlifts WHERE user_id=:id", {"id":user_id}).fetchone()

def isNewMax(weight, previous):
    return weight > previous