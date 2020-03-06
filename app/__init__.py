from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main.routes import main
    from app.robots.routes import robots

    app.register_blueprint(main)
    app.register_blueprint(robots)
    app.url_map.strict_slashes = False

    return app
