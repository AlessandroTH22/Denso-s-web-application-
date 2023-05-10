from flask.globals import session
from src.models.user import User
from src.models.candidato import Candidato
from src.models.session import Session
from database import db
import sqlalchemy

class UserServices:
    @staticmethod
    def get_user():
        user = User.current_user()
        if not user:
            return {"message":"Usuario inexistente", "data":user}

        return {"message":"Usuario encontrado", "data":user}

    @staticmethod
    def get_user2(idUser):
        user2 = User.query.filter_by(id=idUser).first()
        
        
        if not user2:
            return {"message":"Usuario inexistente", "data":user2}

        print(user2)
        return {"message":"Usuario encontrado", "data":user2}

    @staticmethod
    def create_user(name, apellido, email, carrera, ciudad, estado, codigo_postal, telefono, genero, password, validate_password):

        if password != validate_password:
            return {"message":"Las contraseñas son diferentes", "success":False}, 400
         
        new_user = User(name=name, apellido=apellido, email=email, carrera=carrera, ciudad=ciudad, estado=estado, codigo_postal=codigo_postal, telefono=telefono, genero=genero,  password=password, administrador=0)

        db.session.add(new_user)
        db.session.commit()

        return {"message":"Usuario creado correctamente", "success":True}

    @staticmethod
    def get_userAll():
       user = User.query.all() 
       if not user:
           return {"message":"Juego inexistente", "data":user}

       return {"message":"Juego encontrado", "data":user}


    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message":"Usuario no encontrado", "success":False}, 404
        
        if not user.check_password(password):
            return {"message":"Contraseña incorrecta", "success":False}, 404

        session = Session.open()
        session.set("user_id",user.id )
        session.save()

        print(session.get("token"))
        
        return {"message":"Login exitoso","token":session.get("token"), "success":True} 


    @staticmethod
    def loginAdmin(email, password):
        user = User.query.filter_by(email=email,administrador=1).first()

        if not user:
            return {"message":"Usuario no encontrado", "success":False}, 404

        if not user.check_password(password):
            return {"message":"Contraseña incorrecta", "success":False}, 404
        
        session = Session.open()
        session.set("user_id",user.id )
        session.save()

        print(session.get("token"))
        
        return {"message":"Login exitoso","token":session.get("token"), "success":True} 


