from flask.globals import session
from src.models.prueba import Prueba
from src.models.candidato import Candidato
from src.models.session import Session
from database import db


class PruebaServices:

    @staticmethod
    def get_prueba(idPrueba):
        prueba = Prueba.query.filter_by(id_prueba=idPrueba).first()
        
        if not prueba:
            return {"message":"Prueba inexistente", "data":prueba}

        print(prueba)
        return {"message":"Prueba encontrado", "data":prueba}




    @staticmethod
    def create_prueba(nombre):
         
        new_prueba = Prueba(nombre=nombre)

        db.session.add(new_prueba)
        db.session.commit()
        return {"message":"Prueba creada correctamente", "success":True}


