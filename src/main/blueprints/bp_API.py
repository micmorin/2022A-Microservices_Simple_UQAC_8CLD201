from flask import Blueprint
from main.controllers import API_cont

bp_api = Blueprint('api', __name__, url_prefix="/api")

bp_api.route('/',                             methods=['GET'])       (API_cont.all)
bp_api.route('/<int:id>',                     methods=['GET'])       (API_cont.one)
bp_api.route('/',                             methods=['PUT'])       (API_cont.create)
bp_api.route('/',                             methods=['POST'])      (API_cont.update)
bp_api.route('/<int:id>',                     methods=['DELETE'])    (API_cont.destroy)