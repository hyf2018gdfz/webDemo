from flask import Flask

def create_app():
    app = Flask(__name__,static_folder="static", template_folder="templates")
    # app.config.from_object('config.Config')

    from .routes.main import main

    app.register_blueprint(main, url_prefix='/')
    return app