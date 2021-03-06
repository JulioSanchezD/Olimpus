from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
import eventlet
eventlet.monkey_patch()

# Create an ORM connection to the database
db = SQLAlchemy()

# Creation and configuration of login session
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
login_manager.login_message = "Please log in"

# Create a bcrypt object for encrypting passwords
bcrypt = Bcrypt()

# Wrapps the flask application using a web socket from socketio
socketio = SocketIO()

# Create MQTT broker instance
mqtt = Mqtt()


def create_app():
    app = Flask(__name__)

    app.secret_key = "algo que cambiaremos despues martin"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_TLS_ENABLED'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)
    mqtt.init_app(app)

    mqtt.publish("test", 'Starting flask-mqtt server...'.encode('utf-8'))

    from app.main.routes import main
    from app.robots.routes import robots
    from app.communications.routes import communications

    app.register_blueprint(main)
    app.register_blueprint(robots)
    app.register_blueprint(communications)
    # app.url_map.strict_slashes = False # TODO delete?

    return app
