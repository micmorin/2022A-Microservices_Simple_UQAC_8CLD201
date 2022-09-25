from flask import Blueprint
from main.controllers import calculs_cont

bp_objects = Blueprint('calculs', __name__,url_prefix="/calculs")

bp_objects.route("/calculs/")       (calculs_cont.create)
bp_objects.route("/calculs/list")   (calculs_cont.index)
bp_objects.route("/calculs/delete") (calculs_cont.destroy)