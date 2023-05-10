from flask.globals import session
from src.models.user import User
from src.models.candidato import Candidato
from src.models.session import Session
from database import db

import sqlalchemy

class DeleteServices:
    @staticmethod
    def deleteUser(myid):
        delete = db.session.execute(sqlalchemy.text("CALL SP_BorrarUsuarioF(:param)"), {"param":myid}).fetchall()
        db.session.commit()
        print(myid)
        if not delete:
            return {"message":"Usuario inexistente"}

        return {"message":"Usuario eliminado"}
        

   