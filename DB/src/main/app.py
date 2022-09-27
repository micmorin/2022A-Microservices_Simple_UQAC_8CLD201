# APPLICATION FACTORY

from flask import Flask
from main.app_init import database
from main.blueprints.bp_default import bp_default
from main.blueprints.bp_users import bp_users
from main.blueprints.bp_profil import bp_profil
from main.blueprints.bp_calculs import bp_calculs

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    database.init_app(app)

    app.register_blueprint(bp_default)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_profil)
    app.register_blueprint(bp_calculs)

    return app