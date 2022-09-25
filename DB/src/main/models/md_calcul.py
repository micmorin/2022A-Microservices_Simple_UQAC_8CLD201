from main.app_init.database import db
from main.models.md_user import User
from datetime import datetime

class Calcul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    result = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Calcul %r>' % self.name

    def to_json(self):
        user = User.query.get_or_404(self.user_id)
        return {"id":self.id,
                "body":self.body,
                "result":self.result,
                "date":self.date,
                "user":user.to_json()}
