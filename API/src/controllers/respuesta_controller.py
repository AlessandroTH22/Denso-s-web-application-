from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.respuesta_service import RespuestaServices

class RespuestaDto:
    respuesta = {
        "id_respuesta":fields.String,
        "descripcion":fields.String,
        "puntos":fields.String,
        "id_instancia":fields.String,
        "id_pregunta":fields.String,
    }

    response = {
        "data": fields.Nested(respuesta),
        "message":fields.String
    }
    
class RespuestaController(Resource):
    def post(self):
        data = request.json
        print(data)
        return RespuestaServices.create_respuesta(data["descripcion"], data["puntos"], data["id_instancia"], data["id_pregunta"])
    
 
class ObtenerRespuesta(Resource):
    @marshal_with(RespuestaDto.response)
    def get(self, idInstancia):
        return RespuestaServices.get_respuesta(idInstancia)