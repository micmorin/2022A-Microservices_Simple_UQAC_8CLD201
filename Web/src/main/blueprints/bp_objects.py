from flask import Blueprint
from main.controllers import object_cont

bp_objects = Blueprint('objects', __name__,url_prefix="/objects")

bp_objects.route('/',                     methods=['GET'])        (object_cont.index)
bp_objects.route('/create',               methods=['GET'])        (object_cont.create)
bp_objects.route('/store',                  methods=['POST'])       (object_cont.store)
bp_objects.route('/<int:object_id>',        methods=['GET'])        (object_cont.show)
bp_objects.route('/<int:object_id>/edit',   methods=['GET','POST']) (object_cont.update)
bp_objects.route('/<int:object_id>',        methods=['POST'])       (object_cont.destroy)