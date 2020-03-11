from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Create an ORM connection to the database
db = SQLAlchemy()

# Creation and configuration of login session
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
login_manager.login_message = "Please log in"

# Create a bcrypt object for encrypting passwords
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.secret_key = "algo que cambiaremos despues martin"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.main.routes import main
    from app.robots.routes import robots

    app.register_blueprint(main)
    app.register_blueprint(robots)
    # app.url_map.strict_slashes = False # TODO delete?

    return app
