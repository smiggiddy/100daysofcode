from flask_sqlalchemy import SQLAlchemy
from . import db


# class User(db.Model):
#     # TODO create class for user login
#     pass


class ToDoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    note_hash = db.Column(db.String(16), nullable=False, unique=True)
    name = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    items_list = db.relationship('Tasks')


class Tasks(db.Model):
    __tablename__ = 'listtasks'
    id = db.Column(db.Integer, primary_key=True)
    list_item_name = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Integer)
    todo_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)

