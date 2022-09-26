from queue import Empty
from main.models.md_profil import Profil
from main.models.md_user import User
from flask import  request, jsonify
from main.app_init.database import db

def prof_array(message):
    profils = Profil.query.all()
    if profils is Empty:
        return jsonify({"message":"no profile found"}), 404
    else:
        profils_obj = []
        for p in profils:
            profils_obj.append(p.to_json())
        return jsonify({"message":message, "data": profils_obj}), 200

def index(usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin":
        return prof_array("ok")
    else:
        return jsonify({"message":"Must be admin"}),503

def createProfil(usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin":
        p = Profil(
            description=request.form['description']
            )
        db.session.add(p)
        db.session.commit()
        return prof_array("Profil enregistre!")
    else:
        return jsonify({"message":"Must be admin"}),503

def updateProfil(profil_id,usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin":
        p = Profil.query.get_or_404(profil_id)
        p.description = request.form['description']
        db.session.commit()
        return prof_array("Le profil a ete mis a jour")
    else:
        return jsonify({"message":"Must be admin"}),503

def destroyProfil(profil_id,usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if  u.profil.description == "admin":
        p = Profil.query.get_or_404(profil_id)
        users = User.query.filter_by(profil_id=profil_id).all()
        if users == []:
            db.session.delete(p)
            db.session.commit()
            return prof_array("Le profil a ete supprime!")
        else:
            return jsonify({"message":"Le profil est utilise par un utilisateur!"}), 403 
    else:
        return jsonify({"message":"Must be admin"}),503