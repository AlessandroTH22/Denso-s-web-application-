from database import db, bcrypt
from flask import request

from .session import Session


class Instancia_prueba(db.Model):
    __tablename__ = "instancia_prueba"
    id_instancia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Integer, nullable=True)
    puntajeTotal = db.Column(db.Integer, nullable=True)
    nivelDesarrollo = db.Column(db.String(255), nullable=True)
    id_prueba = db.Column(db.Integer, db.ForeignKey("prueba.id_prueba"))
    id = db.Column(db.Integer, db.ForeignKey("user.id"))

 