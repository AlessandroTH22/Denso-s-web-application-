from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.instancia_service import InstanciaServices
from src.models.pregunta import Pregunta

class InstanciaDto:
    instancia = {
        "id_instancia":fields.String,
        "fecha":fields.String,
        "puntajeTotal":fields.String,
        "nivelDesarrollo":fields.String,
        "id_prueba":fields.String,
        "id":fields.String,
    }

    instanciaS = {
        "nivelDesarrollo":fields.String,
        "puntajeTotal":fields.String,
        "fecha":fields.String,
        "id":fields.String,
        "name":fields.String,
    }

    instanciaRP = {
        "id_instancia":fields.String,
        "Pregunta":fields.String,
        "Respuesta":fields.String,
        "puntos":fields.String,
        "fecha":fields.String,
        "nombre":fields.String,
    }

    instanciaNivel = {
        "id":fields.String,
        "name":fields.String,
        "apellido":fields.String,
        "puntajeTotal":fields.String,
        "nivelDesarrollo":fields.String,
        "fecha":fields.String,
    }

    response = {
        "data": fields.Nested(instancia),
        "message":fields.String
    }

    response2 = {
        "data": fields.Nested(instanciaS),
        "message":fields.String
    }
    response3 = {
        "data": fields.Nested(instanciaRP),
        "message":fields.String
    }

    response4 = {
        "data": fields.Nested(instanciaNivel),
        "message":fields.String
    }
    
class InstanciaController(Resource):
    def post(self):
        data = request.json
        print(data)
        return InstanciaServices.create_instancia(data["puntajeTotal"], data["nivelDesarrollo"],data["id_prueba"],data["id"])
    
class ObtenerInstancia(Resource):
     @marshal_with(InstanciaDto.response)
     def get(self, idUser):
         return InstanciaServices.get_instancia(idUser)


class ObtenerInstanciaS(Resource):
     @marshal_with(InstanciaDto.response2)
     def get(self):
         return InstanciaServices.get_instanciaS()

class ObtenerLiderazgoAll(Resource):
     @marshal_with(InstanciaDto.response2)
     def get(self):
         return InstanciaServices.get_liderazgoAll()


class ObtenerInstanciaP(Resource):
     @marshal_with(InstanciaDto.response2)
     def get(self):
         return InstanciaServices.get_instanciaP()

class ObtenerRespuestasLiderazgo(Resource):
     @marshal_with(InstanciaDto.response3)
     def get(self,myid):
         return InstanciaServices.get_respuestasLiderazgo(myid)

class ObtenerRespuestasPersonalidad(Resource):
     @marshal_with(InstanciaDto.response3)
     def get(self,myid):
         return InstanciaServices.get_respuestasPersonalidad(myid)


class ObtenerPersonalidadAll(Resource):
     @marshal_with(InstanciaDto.response2)
     def get(self):
         return InstanciaServices.get_personalidadAll()



class ObtenerLiderazgoAlto(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_liderazgoAlto()

class ObtenerLiderazgoMedio(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_liderazgoMedio()

class ObtenerLiderazgoBajo(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_liderazgoBajo()

class ObtenerE(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_E()

class ObtenerS(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_S()

class ObtenerF(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_F()

class ObtenerP(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_P()


class ObtenerI(Resource):
     @marshal_with(InstanciaDto.response4)
     def get(self):
         return InstanciaServices.get_I()

class ObtenerN(Resource):
    @marshal_with(InstanciaDto.response4)
    def get(self):
         return InstanciaServices.get_N()

class ObtenerT(Resource):
    @marshal_with(InstanciaDto.response4)
    def get(self):
         return InstanciaServices.get_T()

class ObtenerJ(Resource):
    @marshal_with(InstanciaDto.response4)
    def get(self):
         return InstanciaServices.get_J()


