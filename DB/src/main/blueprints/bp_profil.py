from flask import Blueprint
from main.controllers import admin_cont

bp_profil = Blueprint('profil', __name__,url_prefix="/profil/<string:usertoken>")

bp_profil.route('/',                               methods=['GET'])       (admin_cont.index)
bp_profil.route('/create',                  methods=['POST'])      (admin_cont.createProfil)
bp_profil.route('/<int:profil_id>/edit/',   methods=['POST'])      (admin_cont.updateProfil)
bp_profil.route('/<int:profil_id>/',        methods=['POST'])      (admin_cont.destroyProfil)