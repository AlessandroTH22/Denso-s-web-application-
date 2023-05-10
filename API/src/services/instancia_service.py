from flask.globals import session
from src.models.instancia_prueba import Instancia_prueba
from src.models.candidato import Candidato
from src.models.session import Session
from datetime import date
from flask import request
from database import db
import sqlalchemy


class InstanciaServices:
    @staticmethod
    def get_instancia(idUser):
        instancia = Instancia_prueba.query.filter_by(id=idUser).all()
        
        if not instancia:
            return {"message":"Instancia inexistente", "data":instancia}

        return {"message":"Instancia encontrada", "data":instancia}

    @staticmethod
    def create_instancia(puntajeTotal,nivelDesarrollo,id_prueba, id):

        auth_token = request.headers.get('Authorization')
        session = Session.open(auth_token)
        
        new_instancia = Instancia_prueba(fecha=date.today(), puntajeTotal=puntajeTotal, nivelDesarrollo=nivelDesarrollo, id_prueba=id_prueba, id=id)

        db.session.add(new_instancia)
        db.session.commit()

        return {"message":"Instancia creada correctamente", "success":True}


    @staticmethod
    def get_instanciaS():
        auth_token = request.headers.get('Authorization')
        sessio = Session.open(auth_token)
        instancia = db.session.execute(sqlalchemy.text("CALL SP_Liderazgo(:param)"), {"param":sessio.get("user_id")}).fetchall()
        
        if not instancia:
            return {"message":"Instancia inexistente", "data":instancia}

        return {"message":"Instancia encontrada", "data":instancia}


    @staticmethod
    def get_instanciaP():
        auth_token = request.headers.get('Authorization')
        sessio = Session.open(auth_token)
        instancia = db.session.execute(sqlalchemy.text("CALL SP_Personalidad(:param)"), {"param":sessio.get("user_id")}).fetchall()
        
        if not instancia:
            return {"message":"Instancia inexistente", "data":instancia}

        return {"message":"Instancia encontrada", "data":instancia}


    @staticmethod
    def get_liderazgoAll():
        liderazgo = db.session.execute(sqlalchemy.text("CALL SP_LiderazgoAll()")).fetchall()
        
        if not liderazgo:
            return {"message":"Instancia inexistente", "data":liderazgo}

        return {"message":"Instancia encontrada", "data":liderazgo}
    
    @staticmethod
    def get_personalidadAll():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_PersonalidadAll()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}


    @staticmethod
    def get_respuestasPersonalidad(myid):
        instancia = db.session.execute(sqlalchemy.text("CALL SP_ObtenerRespuestasPersonalidad(:param)"), {"param":myid}).fetchall()
        
        if not instancia:
            return {"message":"Instancia inexistente", "data":instancia}

        return {"message":"Instancia encontrada", "data":instancia}

    @staticmethod
    def get_respuestasLiderazgo(myid):
        instancia = db.session.execute(sqlalchemy.text("CALL SP_ObtenerRespuestasLiderazgo(:param)"), {"param":myid}).fetchall()
        
        if not instancia:
            return {"message":"Instancia inexistente", "data":instancia}

        return {"message":"Instancia encontrada", "data":instancia}

    @staticmethod
    def get_liderazgoAlto():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosLiderazgoAltoP1()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_liderazgoMedio():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosLiderazgoMedioP1()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_liderazgoBajo():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosLiderazgoBajoP1()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}


    @staticmethod
    def get_E():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosExtrovertidosP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_S():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosSensacionP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    
    @staticmethod
    def get_F():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosSentimentalesP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_P():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosPercepcionP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}


    @staticmethod
    def get_I():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosIntrovertidosP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_N():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosIntuicionP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_T():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosPensamientoP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}

    @staticmethod
    def get_J():
        personalidad = db.session.execute(sqlalchemy.text("CALL SP_CandidatosJuicioP2()")).fetchall()

        if not personalidad:
            return {"message":"Instancia inexistente", "data":personalidad}

        return {"message":"Instancia encontrada", "data":personalidad}





    