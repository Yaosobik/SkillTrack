from flask import Flask
from .extensions import db, migrate
from .config import Config

from app.routes.user import student, teacher
from app.routes.task import task
from app.routes.main import main


# ⁡⁣⁢⁣ТАЙМ КОД НА КОТОРОМ ОСТАНОВИЛСЯ 𝟮:𝟰𝟰:𝟱𝟳⁡


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(student)
    app.register_blueprint(teacher)
    app.register_blueprint(task)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
