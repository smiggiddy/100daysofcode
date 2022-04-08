from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



db = SQLAlchemy()
DB_NAME = "todolist.db"


def create_app():
    app = Flask(__name__)

    # Connect to DB 
    # TODO Connect database to docker mysql / maria db mysql://username:password@server/db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret'

    db.init_app(app)

    # import views #TODO create views etc
    from .views import views 

    #TODO register app blueprints
    app.register_blueprint(views, url_prefix='/')

    
    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #TODO create db models
    from .models import ToDoList, Tasks

    create_db(app)

    return app


def create_db(app):
    """Makes sure db exists"""

    if not os.path.exists('./day-88/todo_list/' + DB_NAME):
        db.create_all(app=app)
        print(f'Created TodoList DB {DB_NAME}')

