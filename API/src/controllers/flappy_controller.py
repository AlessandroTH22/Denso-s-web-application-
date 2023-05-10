from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.flappy_service import FlappyServices

class FlappyDto:
    flappy = {
        "id_flappy":fields.String,
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
        "data": fields.Nested(flappy),
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
    
class FlappyController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return FlappyServices.create_flappy(data["num_intentos"], data["puntaje"], data["id"])
    
    @marshal_with(FlappyDto.response)
    def get(self):
        return FlappyServices.get_flappy()


class FlappyControllerAll(Resource):
    
    @marshal_with(FlappyDto.response)
    def get(self):
        return FlappyServices.get_flappyAll()


class FlappyRank(Resource):
    @marshal_with(FlappyDto.response2)
    def get(self):
        return FlappyServices.get_flappyRank()

class Flappy10(Resource):
    @marshal_with(FlappyDto.response2)
    def get(self):
        return FlappyServices.get_flappy10()

class FlappyMax(Resource):
    @marshal_with(FlappyDto.response3)
    def get(self,myid):
        return FlappyServices.get_flappyMax(myid)