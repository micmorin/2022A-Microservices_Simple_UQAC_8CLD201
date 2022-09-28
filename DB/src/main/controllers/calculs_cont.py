from queue import Empty
from unicodedata import ucd_3_2_0
from main.models.md_calcul import Calcul
from main.models.md_user import User
from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify
from main.app_init.database import db

def calcul_array(message, u):
    calc = Calcul.query.filter_by(user=u).all()
    if calc is Empty:
        return jsonify({"message":"no calculations found"}), 404
    else:
        calc_obj = []
        for c in calc:
            calc_obj.append(c.to_json())
        return jsonify({"message":message, "data": calc_obj}), 200

def index(usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if u is None:
         return jsonify({"message":"user not authenticated"}), 503
    else:
        return calcul_array("ok", u)

def create(usertoken):
    u = User.query.filter_by(token=usertoken).first()
    if u is None:
         return jsonify({"message":"user not authenticated"}), 503
    else:
        try:
            new_calc = Calcul(
                body=request.values.get('body'), 
                result=request.values.get('result'), 
                date=request.values.get('date'),
                user= u
                )
            db.session.add(new_calc)
            db.session.commit()
            return calcul_array('Calcul enregistre!', u)
        except:
            return jsonify({"message":"Un probleme est survenu"}), 400


def destroy(usertoken, id):
    u = User.query.filter_by(token=usertoken).first()
    if u is None:
         return jsonify({"message":"user not authenticated"}), 503
    else:
        toBeChanged = Calcul.query.get_or_404(id)
        if  u.profil.description == "admin" or toBeChanged.user.token==usertoken:
            db.session.delete(toBeChanged)
            db.session.commit()
            return calcul_array("Le calcul a ete supprime!", u)
        else:
            return jsonify({"message":"Must be admin or current user"}), 503