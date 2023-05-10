
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.controllers.user_controller import UserController, UserControllerFindUser, UserLoginController,UserControllerAll, ObtenerUser, UserLoginAdminController

from src.controllers.frogger_controller import FroggerController,FroggerControllerAll, FroggerRank, FroggerMax, Frogger10

from src.controllers.flappy_controller import FlappyController,FlappyControllerAll, FlappyRank, FlappyMax, Flappy10

from src.controllers.pregunta_controller import PreguntaController,ObtenerPregunta

from src.controllers.prueba_controller import PruebaController,ObtenerPrueba

from src.controllers.respuesta_controller import RespuestaController,ObtenerRespuesta

from src.controllers.instancia_controller import InstanciaController,ObtenerInstancia,ObtenerInstanciaS, ObtenerInstanciaP, ObtenerLiderazgoAll, ObtenerRespuestasPersonalidad, ObtenerPersonalidadAll, ObtenerRespuestasLiderazgo, ObtenerLiderazgoAlto, ObtenerLiderazgoMedio, ObtenerLiderazgoBajo, ObtenerE, ObtenerF, ObtenerP, ObtenerS, ObtenerI, ObtenerN, ObtenerT, ObtenerJ

from src.controllers.delete_controller import DeleteUserController


from flask_migrate import Migrate
from database import db, bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1/densodb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

CORS(app)
api = Api(app)
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db, directory="./database/migrations")

"""
Borrar
"""
api.add_resource(DeleteUserController, "/delete/user/<myid>")


"""
Respuesta
"""
api.add_resource(RespuestaController, "/respuesta")
api.add_resource(ObtenerRespuesta, "/respuesta/<idInstancia>")

"""
Instancia
"""
api.add_resource(InstanciaController, "/instancia")
api.add_resource(ObtenerInstancia, "/instancia/<idUser>")
api.add_resource(ObtenerInstanciaS, "/instancia/user")
api.add_resource(ObtenerInstanciaP, "/instancia/user/personalidad")
api.add_resource(ObtenerLiderazgoAll, "/instancia/liderazgo")
api.add_resource(ObtenerPersonalidadAll, "/instancia/personalidad")
api.add_resource(ObtenerRespuestasPersonalidad, "/respuestas/personalidad/<myid>")
api.add_resource(ObtenerRespuestasLiderazgo, "/respuestas/liderazgo/<myid>")
api.add_resource(ObtenerLiderazgoAlto, "/liderazgoAlto")
api.add_resource(ObtenerLiderazgoMedio, "/liderazgoMedio")
api.add_resource(ObtenerLiderazgoBajo, "/liderazgoBajo")
api.add_resource(ObtenerE, "/personalidadE")
api.add_resource(ObtenerS, "/personalidadS")
api.add_resource(ObtenerF, "/personalidadF")
api.add_resource(ObtenerP, "/personalidadP")
api.add_resource(ObtenerI, "/personalidadI")
api.add_resource(ObtenerN, "/personalidadN")
api.add_resource(ObtenerT, "/personalidadT")
api.add_resource(ObtenerJ, "/personalidadJ")


"""
Pregunta
"""
api.add_resource(PreguntaController, "/pregunta")
api.add_resource(ObtenerPregunta, "/pregunta/<idPregunta>")

"""
Prueba
"""

api.add_resource(PruebaController, "/prueba")
api.add_resource(ObtenerPrueba, "/prueba/<idPrueba>")

"""
Flappy
"""
api.add_resource(FlappyController, "/flappy")
api.add_resource(FlappyControllerAll, "/flappy/all")
api.add_resource(FlappyRank, "/flappy/rank")
api.add_resource(FlappyMax, "/flappyMax/<myid>")
api.add_resource(Flappy10, "/flappy10")

"""
Frogger
"""
api.add_resource(FroggerController, "/frogger")
api.add_resource(FroggerControllerAll, "/frogger/all")
api.add_resource(FroggerRank, "/frogger/rank")
api.add_resource(FroggerMax, "/froggerMax/<myid>")
api.add_resource(Frogger10, "/frogger10")

"""
User
"""
api.add_resource(UserController, "/user")
api.add_resource(UserControllerAll, "/user/all")
api.add_resource(UserLoginController, "/user/login")
api.add_resource(UserControllerFindUser, "/user/search")
api.add_resource(ObtenerUser,"/user/<idUser>")
api.add_resource(UserLoginAdminController,"/userAdmin/login")




"""
app
    - models
    - services
    - controllers
application.py
"""