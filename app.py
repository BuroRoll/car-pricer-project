import os
from flask import Flask

import config
from extensions import database, commands
from flask_jwt_extended import JWTManager

# blueprint import
from blueprints.auth.views import auth


def create_app():
    app = Flask(__name__)
    # setup with the configuration provided by the user / environment
    # app.config.from_object(os.environ['APP_SETTINGS'])
    app.config.from_object(config.DevelopmentConfig)
    # app.config.from_object(config.Config)
    # app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET_KEY']
    jwt = JWTManager(app)

    # setup all our dependencies
    database.init_app()
    commands.init_app(app)

    # register blueprint
    app.register_blueprint(auth)

    return app


if __name__ == "__main__":
    create_app().run()
