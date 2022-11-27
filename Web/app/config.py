from os import  path

basedir = path.abspath(path.dirname(__file__))

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = '/templates'
    FLASK_APP = 'run.py'
    SECRET_KEY = "super secret key"


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class URL_Helper():
    DB_URL='http://db:5000'
    Comp_URL='http://complexe:5000'
    Simple_URL='https://xwwt2jr2yj.execute-api.us-east-1.amazonaws.com/default/test'




