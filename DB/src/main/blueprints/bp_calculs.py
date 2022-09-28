from flask import Blueprint
from main.controllers import calculs_cont

bp_calculs = Blueprint('calculs', __name__,url_prefix="/calculs/<string:usertoken>")

bp_calculs.route("/",                               methods=['POST'])     (calculs_cont.index)
bp_calculs.route("/create",                         methods=['POST'])     (calculs_cont.create)
bp_calculs.route("/<int:id>/delete",                methods=['POST'])     (calculs_cont.destroy)