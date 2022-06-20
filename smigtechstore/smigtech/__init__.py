from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = 'smig-store.db'

def create_app():
    """Create then return the app appliance."""

    app = Flask(__name__)

    ## Config DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smig-store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
    db.init_app(app) 

    from .views import views 

    app.register_blueprint(views, url_prefix='/') 


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    from .models import Store

    # create_db(app)

    return app 


def create_db(app):
    """Ensure db exists"""

    if not os.path.exists('./day-96/smigtech' + DB_NAME):
        db.create_all(app=app)
        print(f'Created new db {DB_NAME}')


