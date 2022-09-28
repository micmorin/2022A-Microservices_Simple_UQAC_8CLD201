from main.app_init.database import db


class User():
    u = [0]
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.token)    

    def to_json(self):
        return {"token":self.token}