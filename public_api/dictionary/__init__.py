from flask import Flask 
import os


def create_app():
    app = Flask(__name__)
    from .views import views 

    app.register_blueprint(views, url_prefix='/')

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    return app 