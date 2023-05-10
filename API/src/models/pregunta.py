from database import db, bcrypt, SQLAlchemy
from flask import request

from .session import Session


class Pregunta(db.Model):
    __tablename__ = "pregunta"
    id_pregunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numPregunta = db.Column(db.Integer, nullable=True)
    descripcion = db.Column(db.String(255), nullable=True)
    puntaje = db.Column(db.Integer, nullable=True)
    id_prueba = db.Column(db.Integer, db.ForeignKey("prueba.id_prueba"))
    