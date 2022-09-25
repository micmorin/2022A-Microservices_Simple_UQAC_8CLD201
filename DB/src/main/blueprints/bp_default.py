from flask import Blueprint
from main.controllers import default_cont

bp_default = Blueprint('default',__name__, url_prefix="/")

bp_default.route("/")(default_cont.index)
bp_default.route("/login/<string:username>/<string:password>", methods=['POST'])(default_cont.login)
#bp_default.route("/calculs/")(default_cont.index)
#bp_default.route("/calculs/list")(default_cont.index)
#bp_default.route("/calculs/delete")(default_cont.index)