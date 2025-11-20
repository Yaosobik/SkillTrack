from flask import Flask  # , render_template
from .extensions import db
from .config import Config

from .routes import student, teacher


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(student)
    app.register_blueprint(teacher)

    with app.app_context():
        db.create_all()

    return app
