from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return "name"        
    else:
        if check_password_hash(user.password, password):
            session["username"] = username
            session["id"] = user.id
            return True
        else:
            return "password"

def logout():
    del session["username"]
    del session["id"]

def register(username, password):
    #TODO: Form username input listener for unique names 
    try:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        
    except:
        return False

    return login(username, password)