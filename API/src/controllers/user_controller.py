from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.user_service import UserServices

class UserDto:
    candidato = {
        "name":fields.String,
        "apellido":fields.String,
        "email":fields.String,
        "carrera":fields.String,
        "ciudad":fields.String,
        "estado":fields.String,
        "telefono":fields.String,
        "genero":fields.String,
        "codigo_postal": fields.String,

    }

    user = {
        "id":fields.String,
        "name":fields.String,
        "apellido":fields.String,
        "email":fields.String,
        "carrera":fields.String,
        "ciudad":fields.String,
        "estado":fields.String,
        "telefono":fields.String,
        "genero":fields.String,
        "codigo_postal": fields.String,

        "candidatos": fields.List(fields.Nested(candidato)),
    }

    response = {
        "data": fields.Nested(user),
        "message":fields.String
    }
    
class UserController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return UserServices.create_user(data["name"], data["apellido"], data["email"], data["carrera"], data["ciudad"], data["estado"], data["codigo_postal"], data["telefono"], data["genero"], data["password"], data["validate_password"])
    
    @marshal_with(UserDto.response)
    def get(self):
        
        return UserServices.get_user()

class UserControllerFindUser(Resource):
    @marshal_with(UserDto.response)
    def post(self):
        data = request.json
        return UserServices.get_user(data["id"])


class UserLoginController(Resource):
    def post(self):
        data = request.json
        print(data)
        return UserServices.login(data["email"], data["password"])


class UserLoginAdminController(Resource):
    def post(self):
        data = request.json
        print(data)
        return UserServices.loginAdmin(data["email"], data["password"])


class UserControllerAll(Resource):
    
    @marshal_with(UserDto.response)
    def get(self):
        return UserServices.get_userAll()


class ObtenerUser(Resource):
     @marshal_with(UserDto.response)
     def get(self, idUser):
         return UserServices.get_user2(idUser)
