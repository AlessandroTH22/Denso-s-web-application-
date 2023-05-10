from database import db
from flask import request
from .session import Session


class Prueba(db.Model):
    __tablename__ = "prueba"
    id_prueba = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=True)
    
