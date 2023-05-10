from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.prueba_service import PruebaServices

class PruebaDto:
    prueba = {
        "id_prueba":fields.String,
        "nombre":fields.String,
    }

    response = {
        "data": fields.Nested(prueba),
        "message":fields.String
    }
    
class PruebaController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return PruebaServices.create_prueba(data["nombre"])
    
  

class ObtenerPrueba(Resource):
    @marshal_with(PruebaDto.response)
    def get(self, idPrueba):
        return PruebaServices.get_prueba(idPrueba)