# APPLICATION FACTORY

from flask import Flask
from main.app_init import apparence, database, login
from main.blueprints.bp_default import bp_default
from main.blueprints.bp_users import bp_users
from main.blueprints.bp_calculs import bp_calculs
from main.blueprints.bp_profil import bp_profil

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    apparence.init_app(app)
    database.init_app(app)
    login.init_app(app)

    app.register_blueprint(bp_default)
    app.register_blueprint(bp_calculs)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_profil)

    return app