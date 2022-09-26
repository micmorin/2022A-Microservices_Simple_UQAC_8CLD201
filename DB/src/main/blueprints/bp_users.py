from flask import Blueprint
from main.controllers import user_cont

bp_users = Blueprint('users', __name__,url_prefix="/users/<string:usertoken>")

bp_users.route('/',                     methods=['GET'])        (user_cont.index)
bp_users.route('/create',               methods=['POST'])       (user_cont.create)
bp_users.route('/<int:user_id>/edit',   methods=['GET','POST']) (user_cont.update)
bp_users.route('/<int:user_id>',        methods=['POST'])       (user_cont.destroy)