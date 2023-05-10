from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.delete_service import DeleteServices

class DeleteDto:
    response = {
        "message":fields.String
    }
    
class DeleteUserController(Resource):
    @marshal_with(DeleteDto.response)
    def get(self,myid):
        return DeleteServices.deleteUser(myid)

