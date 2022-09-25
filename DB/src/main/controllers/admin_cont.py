from main.models.md_profil import Profil
from main.models.md_user import User
from flask import render_template, request, redirect, url_for, flash, jsonify
from main.app_init.database import db

def index(usertoken):
    u = User.query.get_or_404(token=usertoken)
    if  u.profil.description == "admin":
        return jsonify({"message":"ok", "data": Profil.query.all()}), 200
    else:
        return jsonify({"message":"Must be admin"}),503

def createProfil(usertoken):
    u = User.query.get_or_404(token=usertoken)
    if  u.profil.description == "admin":
        p = Profil(
            description=request.form['description']
            )
        db.session.add(p)
        db.session.commit()
        return jsonify({"message":"Profil enregistre!", "data": Profil.query.all()}), 200
    else:
        return jsonify({"message":"Must be admin"}),503

def updateProfil(profil_id,usertoken):
    u = User.query.get_or_404(token=usertoken)
    if  u.profil.description == "admin":
        p = Profil.query.get_or_404(profil_id)
        if request.method == 'POST':
            p.description = request.form['description']
            db.session.commit()
            return jsonify({"message":"Le profil a ete mis a jour", "data": Profil.query.all()}), 200
        return jsonify({"message":"ok", "data": Profil.query.all()}), 200
    else:
        return jsonify({"message":"Must be admin"}),503

def destroyProfil(profil_id,usertoken):
    u = User.query.get_or_404(token=usertoken)
    if  u.profil.description == "admin":
        p = Profil.query.get_or_404(profil_id)
        users = User.query.filter_by(profil_id=profil_id).all()
        if users == []:
            db.session.delete(p)
            db.session.commit()
            return jsonify({"message":"Le profil a ete supprime!", "data": Profil.query.all()}), 200
        else:
            return jsonify({"message":"Le profil est utilise par un utilisateur!"}), 403 
    else:
        return jsonify({"message":"Must be admin"}),503