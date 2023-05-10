from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.pregunta_service import PreguntaServices
from src.models.pregunta import Pregunta

class PreguntaDto:
    pregunta = {
        "id_pregunta":fields.String,
        "numPregunta":fields.String,
        "descripcion":fields.String,
        "puntaje":fields.String,
        "id_prueba":fields.String,
    }

    response = {
        "data": fields.Nested(pregunta),
        "message":fields.String
    }
    
class PreguntaController(Resource):
    def post(self):
        data = request.json
        print(data)
        return PreguntaServices.create_pregunta(data["numPregunta"], data["descripcion"], data["id_prueba"])
    
class ObtenerPregunta(Resource):
     @marshal_with(PreguntaDto.response)
     def get(self, idPregunta):
         return PreguntaServices.get_pregunta(idPregunta)

