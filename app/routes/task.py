from flask import Blueprint
from ..extensions import db
from ..models.task import Task

task = Blueprint("task", __name__)


@task.route("/task/<topic>")
def create_task(topic):
    task = Task(topic=topic)
    db.session.add(task)
    db.session.commit()
    return "Задание успешно создано!"
