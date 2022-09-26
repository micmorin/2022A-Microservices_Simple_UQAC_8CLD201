from main.app_init.database import db
from main.models.md_user import User
from datetime import datetime

class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    setup_date = db.Column(db.Date, nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Object %r>' % self.name

    def to_json(self):
        user = User.query.get_or_404(self.user_id)
        return {"id":self.id,
                "name":self.name,
                "setup_date":self.setup_date,
                "upload_date":self.upload_date,
                "status":self.status,
                "user":user.to_json()}
