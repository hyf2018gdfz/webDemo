from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.main import main
    from .routes.api import api

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')
    return app