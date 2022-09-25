from flask_login import current_user, login_required
from main.models.md_user import User
from main.models.md_object import Object
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from main.app_init.database import db

@login_required
def index():
    return redirect(url_for('default.login'))

@login_required
def create():
    return render_template('object_create.html')

@login_required
def store():
    if current_user.profil.description == 'admin':
        user = User.query.get_or_404(request.values.get('userID'))
        if request.values.get('status') == 'on':
                status = True
        else:
            status=False 
        new_object = Object (
            name=request.values.get('name'),
            status=status,
            setup_date = datetime.date(datetime.utcnow()),
            upload_date =datetime.date(datetime.utcnow()),
            user=user
            )
        db.session.add(new_object)
        db.session.commit()
        flash('Object Créé!')
    return redirect(url_for('default.index'))
            
@login_required
def show(object_id):
    object = Object.query.get_or_404(object_id)
    return render_template('object_show.html', object=object)

@login_required
def update(object_id):
    object = Object.query.get_or_404(object_id)
    if request.method == 'POST' and current_user.profil.description == "admin":
        object.name = request.form['name']
        if request.values.get('status') == 'on':
                object.status = True
        else:
            object.status=False 
        db.session.commit()
        flash("L'objet " + object.name + " a ete mis a jour") 
    return render_template('object_show.html', object=object)   

@login_required
def destroy(post_id):
    return render_template('index.html')