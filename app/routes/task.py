from flask import Blueprint, render_template
from app.extensions import db
from app.models.task import Task

task = Blueprint("task", __name__)


@task.route("/task/create", methods=["POST"])
def create_task():
    return render_template("create_task.html")
