# coding=utf-8

try:
    from main.app import create_app
    from main.app_init.database import db
    from main.models.md_user import User
    from main.models.md_object import Object
    from main.models.md_profil import Profil
    from datetime import datetime
    from werkzeug.security import generate_password_hash


    app = create_app()
    print('Création de la base de données...')
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
            password=generate_password_hash("user"))

        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()

        print('Ajout d\'objet...')
        
        o1 = Object(
            name ='CameraTablotSagueneens', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = True,
            user = admin
        )

        o2 = Object(
            name ='CameraTablotRoitelets', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = True,
            user = admin
        )

        o3 = Object(
            name ='CameraTablotUniversite', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = True,
            user = admin
        )

        o4 = Object(
            name ='CameraUniversiteBegin', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = True,
            user = admin
        )

        o5 = Object(
            name ='CameraUniversiteStPaul', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = False,
            user = admin
        )

        o6 = Object(
            name ='CameraStPaulBarrette', 
            setup_date = datetime.date(datetime.utcnow()),
            upload_date = datetime.date(datetime.utcnow()),
            status = True,
            user = admin
        )

        db.session.add(o1)
        db.session.add(o2)
        db.session.add(o3)
        db.session.add(o4)
        db.session.add(o5)
        db.session.add(o6)
        db.session.commit()

        print('ok, tout est prêt. Vous pouvez exécuter l\'application maintenant.')
        input()

except Exception as e:
    print(e, type(e))
    input()