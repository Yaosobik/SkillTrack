from flask import Blueprint, render_template, request, jsonify, current_app
from ..extensions import db
from ..models.task import Task
from datetime import datetime

task = Blueprint("task", __name__, url_prefix="/task")


@task.route("/create", methods=["GET", "POST"])
def create_topic():
    if request.method == "POST":
        current_app.logger.info("POST /task/create received")
        topic = request.form.get("topic")
        task_text = request.form.get("task")
        group = request.form.get("group")
        deadline_str = request.form.get("deadline")
        max_score = request.form.get("max_score")

        deadline = None
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            except ValueError:
                return "Неверный формат даты (YYYY-MM-DD)", 400

        new_task = Task(
            topic=topic,
            task=task_text,
            group=group,
            deadline=deadline,
            max_score=str(max_score) if max_score is not None else None,
        )

        try:
            db.session.add(new_task)
            db.session.commit()
            current_app.logger.info("Task saved id=%s", new_task.id)
            return jsonify({"status": "created", "id": new_task.id}), 201
        except Exception as e:
            db.session.rollback()
            current_app.logger.exception("Ошибка при сохранении задачи")
            return str(e), 500

    # GET — показать страницу с формой (если нужна)
    return render_template("home_teacher_send_task.html")
