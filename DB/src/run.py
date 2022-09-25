from main.app import create_app

from main.app import create_app
from main.app_init.database import db
from main.models.md_user import User
from main.models.md_calcul import Calcul
from main.models.md_profil import Profil
from datetime import datetime
from werkzeug.security import generate_password_hash

if __name__ == "__main__":
    app = create_app()
    """
    db.create_all(app = create_app())
    print('ok!\n')
    with app.app_context():
        print('Ajouter des profils...')
        prof1 = Profil(description="admin")
        prof2 = Profil(description="user")

        db.session.add(prof1)
        db.session.add(prof2)
        db.session.commit()

        print('Ajouter des utilisateurs...')
        admin = User(
            name="admin_nom", username='admin', email='admin@example.com', 
            password=generate_password_hash("admin"), profil=prof1)
        guest = User(
            name="user_nom",username='user', email='guest@example.com', 
            password=generate_password_hash("user"), profil=prof2)


        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()

        c1 = Calcul(body="1+1", result='2', date=datetime.date(datetime.utcnow()), user=admin)
        c2 = Calcul(body="1+2", result='3', date=datetime.date(datetime.utcnow()), user=admin)
        c3 = Calcul(body="1+3", result='4', date=datetime.date(datetime.utcnow()), user=guest)

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()
    #"""
    app.run(host='0.0.0.0',port=5000)