import json
from queue import Empty
from flask import Blueprint, jsonify, request, redirect, url_for
from main.models.md_object import Object
from main.app_init.database import db
from flask_login import current_user, login_required
from datetime import datetime

def all():
    objects = Object.query.all()
    if objects is Empty:
        return jsonify({"message":"no objects found"}), 404
    else:
        objects_obj = []
        for o in objects:
            objects_obj.append(o.to_json())
        return jsonify({"message":"ok", "data": objects_obj}), 200

def one(id):
    object = Object.query.get_or_404(id)
    return jsonify({"message":"ok", 'data':object.to_json()}), 200

@login_required
def create():
    if current_user.profil.description == "admin":
        record = json.loads(request.data)

        object = Object(
            name = record['name'], 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = record['active'],
            user = record['user']
        )
        db.session.add(object)
        db.session.commit()


        return jsonify({"message":"object created", 
                        "id":object.id}),201  
    else:
        return jsonify({"message":"user can not create an object"}),403

@login_required
def update():
    record = json.loads(request.data)
    object = Object.query.get_or_404(record['id'])
    if current_user.profil.description == "admin":   
        
        name = record['name'], 
        upload_date = datetime.date(datetime.utcnow()),
        status = record['active'],
        user = record['user']
        db.session.commit()

    
        return jsonify({"message":"object updated",
                        "id":object.id}),204
    else:
        return jsonify({"message":"user can not update this object"}),403

@login_required
def destroy(id):
    record = json.loads(request.data)
    object = Object.query.get_or_404(record['id'])
    if current_user.profil.description == "admin":  
        db.session.delete(object)
        db.session.commit()

        return jsonify({"message":"object deleted"}),204
    else:
        return jsonify({"message":"user can not delete this object"}),403