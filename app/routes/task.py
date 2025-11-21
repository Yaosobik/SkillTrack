from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.task import Task

task = Blueprint("task", __name__, url_prefix="/task")


@task.route("/create", methods=["GET", "POST"])
def create_topic():
    if request.method == "POST":
        task = request.form.get("task")
        topic = request.form.get("topic")
        group = request.form.get("group")
        deadline = request.form.get("deadline")
        max_score = request.form.get("max_score")

        task = Task(
            group=group, task=task, topic=topic, deadline=deadline, max_score=max_score
        )
        try:
            db.session.add(task)
            db.session.commit()
            redirect(url_for("home_teacher_check_tasks.html"))
        except Exception as e:
            print(str(e))
    else:
        return render_template("/home_teacher_send_task.html")
