from . import db 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(250), nullable=False)
    item_price = db.Column(db.Float, nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)

