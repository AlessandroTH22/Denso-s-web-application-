from flask.globals import session
from src.models.flappy import Flappy
from src.models.session import Session
from datetime import date
from src.services.user_service import UserServices
from flask import request
from database import db
import sqlalchemy


class FlappyServices:
    @staticmethod
    def get_flappy():
        flappy = Flappy.current_flappy()
        
        if not flappy:
            return {"message":"Juego inexistente", "data":flappy}

        return {"message":"Juego encontrado", "data":flappy}


    @staticmethod
    def get_flappyAll():
        flappy = Flappy.query.all()
        
        if not flappy:
            return {"message":"Juego inexistente", "data":flappy}

        return {"message":"Juego encontrado", "data":flappy}


    @staticmethod
    def get_flappyRank():
        flappy = db.session.execute(sqlalchemy.text("CALL SP_RankingFlappy()")).fetchall()
        if not flappy:
            return {"message":"Juego inexistente", "data":flappy}

        return {"message":"Juego encontrado", "data":flappy}

    @staticmethod
    def get_flappyMax(myid):
        flappy = db.session.execute(sqlalchemy.text("CALL SP_FlappyAlto(:param)"), {"param":myid}).first()
        if not flappy:
            return {"message":"Juego inexistente", "data":flappy}

        return {"message":"Juego encontrado", "data":flappy}

    @staticmethod
    def get_flappy10():
        flappy = db.session.execute(sqlalchemy.text("CALL SP_top10Flappy()")).fetchall()
        if not flappy:
            return {"message":"Juego inexistente", "data":flappy}

        return {"message":"Juego encontrado", "data":flappy}


    @staticmethod
    def create_flappy(num_intentos, puntaje, id):

        auth_token = request.headers.get('Authorization')
        session = Session.open(auth_token)

        new_flappy = Flappy(num_intentos=num_intentos, fecha_ultimoIntento = date.today(), puntaje=puntaje, id=id)

        db.session.add(new_flappy)
        db.session.commit()

        return {"message":"Flappy creado correctamente", "success":True}

    
