from main.models.md_user import User
from main.models.md_profil import Profil
from main.models.form_register import RegisterForm
from flask import  request, jsonify
from main.app_init.database import db
from queue import Empty
from werkzeug.security import generate_password_hash

def user_array(message):
    users = User.query.all()
    if users is Empty:
        return jsonify({"message":"no user found"}), 404
    else:
        users_obj = []
        for u in users:
            users_obj.append(u.to_json())
        return jsonify({"message":message, "data": users_obj}), 200

def index(usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin":
        return user_array("ok")
    else:
        return jsonify({"message":"Must be admin"}), 503

def create(usertoken):
    try:
        new_user = User(
            name=request.values.get('name'), 
            username=request.values.get('username'), 
            email=request.values.get('email'),
            password=request.values.get('password'),
            token=generate_password_hash(request.values.get('name'))
            )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":'Utilisateur enregistre!', "token": new_user.token}), 200
    except:
        return jsonify({"message":"Un probleme est survenu"}), 400

def update(user_id, usertoken):
    toBeChanged = User.query.get_or_404(user_id)
    u = User.query.filter_by(token=usertoken).first()
    if request.method == 'POST':
        if  u.profil.description == "admin" or toBeChanged.token==usertoken:
            toBeChanged.name = request.form['name']
            toBeChanged.username = request.form['username']
            toBeChanged.email = request.form['email']
            toBeChanged.password = request.form['password']
            if  u.profil.description == "admin" and request.form['profil'] != "":
                p = Profil.query.get_or_404(request.form['profil'])
                toBeChanged.profil = p
            db.session.commit()
            if  u.profil.description == "admin":
                return user_array("L'utilisateur " + toBeChanged.username + " a ete mis a jour")
            else:
                return jsonify({"message":"L'utilisateur " + toBeChanged.username + " a ete mis a jour"}), 200
    else:
        if  u.profil.description == "admin":
            return user_array("ok")
    return jsonify({"message":"Must be admin or current user"}), 503   

def destroy(user_id, usertoken):
    toBeChanged = User.query.get_or_404(user_id)
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin" or toBeChanged.token==usertoken:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return user_array("L'utilisateur a ete supprime!")
    else:
        return jsonify({"message":"Must be admin or current user"}), 503  
