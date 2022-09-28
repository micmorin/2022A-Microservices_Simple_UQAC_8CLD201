import requests
from main.models.md_user import User
from main.models.md_profil import Profil
from main.models.form_login import LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash

def index():
    return render_template('index.html')

def login():
    form = LoginForm()
    if form.is_submitted():
        requestToDB = requests.get("http://db:5000/login/"+form.username.data+"/"+form.password.data)
        if requestToDB.status_code == 200:
            JSONFromrequest = requestToDB.json()
            user = User(token=JSONFromrequest['token'])
            login_user(user)
            User.u[0] = user
            flash('Connexion reussie')
            return redirect(url_for('default.index')) 
        else:
            flash('Identifiants invalides.')
            return redirect(url_for('default.login')) 
        
        
    return render_template("login.html", form = form)

@login_required
def logout():
    logout_user()
    return redirect('/')

