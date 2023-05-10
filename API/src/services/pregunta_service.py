from flask.globals import session
from src.models.pregunta import Pregunta
from src.models.candidato import Candidato
from src.models.session import Session
from database import db


class PreguntaServices:

    @staticmethod
    def get_pregunta(idPregunta):
        pregunta = Pregunta.query.filter_by(id_pregunta=idPregunta).first()
        
        if not pregunta:
            return {"message":"Pregunta inexistente", "data":pregunta}

        print(pregunta)
        return {"message":"Pregunta encontrado", "data":pregunta}


    @staticmethod
    def create_pregunta(numPregunta, descripcion, id_prueba):
         
        new_pregunta = Pregunta(numPregunta=numPregunta, descripcion=descripcion, id_prueba=id_prueba, puntaje = 3)

        db.session.add(new_pregunta)
        db.session.commit()
        return {"message":"Pregunta creada correctamente", "success":True}


