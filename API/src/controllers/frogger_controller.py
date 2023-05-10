from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.frogger_service import FroggerServices

class FroggerDto:
    frogger = {
        "id_frogger":fields.String,
        "num_intentos":fields.String,
        "fecha_ultimoIntento":fields.String,
        "puntaje":fields.String,
        "id":fields.String,
    }

    rank = {
        "puntaje":fields.String,
        "num_intentos":fields.String,
        "fecha_ultimoIntento":fields.String,
        "Usuario":fields.String,
        "id":fields.String,
    }

    Max = {
        "id":fields.String,
        "Maximo":fields.String,
    }

    response = {
        "data": fields.Nested(frogger),
        "message":fields.String
    }

    response2 = {
        "data": fields.Nested(rank),
        "message":fields.String
    }

    response3 = {
        "data": fields.Nested(Max),
        "message":fields.String
    }



    
    
class FroggerController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return FroggerServices.create_frogger(data["num_intentos"], data["puntaje"], data["id"])
    
    @marshal_with(FroggerDto.response)
    def get(self):
        return FroggerServices.get_frogger()


class FroggerControllerAll(Resource):
    @marshal_with(FroggerDto.response)
    def get(self):
        return FroggerServices.get_froggerAll()


class FroggerRank(Resource):
    @marshal_with(FroggerDto.response2)
    def get(self):
        return FroggerServices.get_froggerRank()

class Frogger10(Resource):
    @marshal_with(FroggerDto.response2)
    def get(self):
        return FroggerServices.get_frogger10()


class FroggerMax(Resource):
    @marshal_with(FroggerDto.response3)
    def get(self,myid):
        return FroggerServices.get_froggerMax(myid)