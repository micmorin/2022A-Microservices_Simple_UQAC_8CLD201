from flask import Blueprint
from main.controllers import profil_cont

bp_profil = Blueprint('profil', __name__,url_prefix="/profil")

bp_profil.route('/',                      methods=['GET'])       (profil_cont.index)
bp_profil.route('/create',                methods=['POST'])      (profil_cont.createProfil)
bp_profil.route('/<int:profil_id>/edit',  methods=['POST'])      (profil_cont.updateProfil)
bp_profil.route('/<int:profil_id>',       methods=['POST'])      (profil_cont.destroyProfil)