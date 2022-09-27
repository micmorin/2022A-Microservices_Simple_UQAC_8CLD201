from main.models.md_user import User
from main.models.md_calcul import calcul
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from main.app_init.database import db

def index(usertoken):
    return redirect(url_for('default.login'))

def create(usertoken):
    return render_template('object_create.html')


def destroy(usertoken, id):
    return render_template('index.html')