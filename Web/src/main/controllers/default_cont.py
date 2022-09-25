import flask
from main.models.md_object import Object
from main.models.md_user import User
from main.models.md_profil import Profil
from main.models.form_login import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash

def index():
    return render_template('index.html')

def login():
    form = LoginForm()
    if form.is_submitted():
        username = form.username.data
        passwd = form.password.data
        user = User.query.filter_by(username=username).first()
        next = flask.request.args.get('next')
        if user and check_password_hash(user.password, passwd):
            login_user(user)
            flash('Connexion reussie')
        else:
            flash('Identifiants invalides.')
            print("invalid login")

        return flask.redirect(next or flask.url_for('default.index')) 
        
    return render_template("login.html", form = form)

@login_required
def logout():
    logout_user()
    return redirect('/')
