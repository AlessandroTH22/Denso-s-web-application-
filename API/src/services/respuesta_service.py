from flask.globals import session
from src.models.respuesta import Respuesta
from src.models.candidato import Candidato
from src.models.session import Session
from datetime import date
from database import db
from flask import request

class RespuestaServices:
    @staticmethod
    def get_respuesta(idInstancia):
        respuesta = Respuesta.query.filter_by(id_instancia=idInstancia).all()
        
        if not respuesta:
            return {"message":"Respuesta inexistente", "data":respuesta}
        return {"message":"Respuesta encontrada", "data":respuesta}

    @staticmethod
    def create_respuesta(descripcion,puntos,id_instancia,id_pregunta):

        auth_token = request.headers.get('Authorization')
        session = Session.open(auth_token)
        
        new_pregunta = Respuesta(descripcion=descripcion, puntos=puntos, id_instancia=id_instancia, id_pregunta=id_pregunta)

        db.session.add(new_pregunta)
        db.session.commit()

        return {"message":"Respuesta creada correctamente", "success":True}
