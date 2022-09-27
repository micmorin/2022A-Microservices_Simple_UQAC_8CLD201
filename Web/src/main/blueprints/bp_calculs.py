from flask import Blueprint
from main.controllers import calculs_cont

bp_calculs = Blueprint('calculs', __name__,url_prefix="/calculs/<string:usertoken>")

bp_calculs.route("/calculs/",                           methods=['POST'])     (calculs_cont.create)
bp_calculs.route("/calculs/list",                       methods=['POST'])     (calculs_cont.index)
bp_calculs.route("/calculs/<int:id>/delete",            methods=['POST'])     (calculs_cont.destroy)