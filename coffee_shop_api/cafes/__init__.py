from gettext import find
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()
DB_NAME = "cafes.db"

def create_app():
    app = Flask(__name__)

    ##Connect to Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # import needed views from 
    from .api_views import api_views
    from .views import views

    # TODO create views and blueprints
    app.register_blueprint(api_views, url_prefix='/api')
    app.register_blueprint(views, url_prefix='/')

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import the db models before creating the database
    from .models import Cafe 

    create_db(app)

    return app


def create_db(app):
    """Makes sure a database exists"""
    if not os.path.exists('./day-87/cafes/' + DB_NAME):
        db.create_all(app=app)
        print(f'Created new DB {DB_NAME}')

