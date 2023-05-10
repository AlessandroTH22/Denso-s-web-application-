from database import db
from flask import request
from .session import Session



class Frogger(db.Model):
    __tablename__ = "frogger"
    id_frogger = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_intentos = db.Column(db.Integer, nullable=True)
    fecha_ultimoIntento = db.Column(db.Date, nullable=True)
    puntaje = db.Column(db.Integer, nullable=True)
    id = db.Column(db.Integer, db.ForeignKey("user.id"))

   
    @staticmethod
    def current_frogger():
        auth_token = request.headers.get('Authorization')
        print(auth_token)

        if auth_token:
            session = Session.open(auth_token)
            
            if session:
                frogger = Frogger.query.filter_by(id=session.get("user_id")).all() 
                return frogger
            return None
        else:
            return None
