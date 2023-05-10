from database import db, bcrypt
from flask import request

from .session import Session


class Respuesta(db.Model):
    __tablename__ = "respuesta"
    id_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=True)
    puntos = db.Column(db.Integer, nullable=True)
    id_instancia = db.Column(db.Integer, db.ForeignKey("instancia_prueba.id_instancia"))
    id_pregunta = db.Column(db.Integer, db.ForeignKey("pregunta.id_pregunta"))

