from flask.globals import session
from src.models.frogger import Frogger
from src.models.session import Session
from datetime import date
from src.services.user_service import UserServices
from flask import request
from database import db
import sqlalchemy


class FroggerServices:
    @staticmethod
    def get_frogger():
        frogger = Frogger.current_frogger()
        
        if not frogger:
            return {"message":"Juego inexistente", "data":frogger}

        return {"message":"Juego encontrado", "data":frogger}

    @staticmethod
    def get_froggerAll():
        frogger = Frogger.query.all()
        
        if not frogger:
            return {"message":"Juego inexistente", "data":frogger}

        return {"message":"Juego encontrado", "data":frogger}

    @staticmethod
    def get_froggerRank():
       frogger = db.session.execute(sqlalchemy.text("CALL SP_RankingFrogger()")).fetchall()
       if not frogger:
           return {"message":"Juego inexistente", "data":frogger}

       return {"message":"Juego encontrado", "data":frogger}


    @staticmethod
    def get_froggerMax(myid):
        frogger = db.session.execute(sqlalchemy.text("CALL SP_FroggerAlto(:param)"), {"param":myid}).first()
        if not frogger:
            return {"message":"Juego inexistente", "data":frogger}

        return {"message":"Juego encontrado", "data":frogger}


    @staticmethod
    def get_frogger10():
        frogger = db.session.execute(sqlalchemy.text("CALL SP_top10Frogger()")).fetchall()
        if not frogger:
            return {"message":"Juego inexistente", "data":frogger}

        return {"message":"Juego encontrado", "data":frogger}


    @staticmethod
    def create_frogger(num_intentos, puntaje, id):

        auth_token = request.headers.get('Authorization')
        session = Session.open(auth_token)

        new_frogger = Frogger(num_intentos=num_intentos, fecha_ultimoIntento = date.today(),puntaje=puntaje, id=id)

        db.session.add(new_frogger)
        db.session.commit()

        return {"message":"Frogger creado correctamente", "success":True}

    
