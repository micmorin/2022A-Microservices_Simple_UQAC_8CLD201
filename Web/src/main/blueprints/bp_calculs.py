from flask import Blueprint
from main.controllers import calculs_cont

bp_calculs = Blueprint('calculs', __name__,url_prefix="/calculs/")

bp_calculs.route("/",                                       methods=['GET'])     (calculs_cont.index)
bp_calculs.route("/calculs/create",                         methods=['POST'])     (calculs_cont.create)
bp_calculs.route("/calculs/<int:id>/delete",                methods=['POST'])     (calculs_cont.destroy)