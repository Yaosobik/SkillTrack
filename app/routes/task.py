from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app,
    redirect,
    url_for,
)
from ..extensions import db
from ..models.task import Task
from ..models.submission import Submission
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
                return "Неверный формат даты", 400

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

    return render_template("home_teacher_send_task.html")


@task.route("/<int:task_id>", methods=["GET"])
def view_task(task_id):
    t = Task.query.get_or_404(task_id)
    return render_template("task_detail.html", task=t)


@task.route("/<int:task_id>/submit", methods=["POST"])
def submit_answer(task_id):
    t = Task.query.get_or_404(task_id)
    answer = request.form.get("answer")
    student_email = request.form.get(
        "email"
    )  # optional, or take from session if you have user system

    if not answer:
        return "Ответ не может быть пустым", 400

    sub = Submission(task_id=t.id, answer=answer, student_email=student_email)
    try:
        db.session.add(sub)
        db.session.commit()
        current_app.logger.info("Submission saved id=%s for task %s", sub.id, t.id)
        return redirect(url_for("main.grades"))  # возвращаемся к списку заданий ученика
    except Exception as e:
        db.session.rollback()
        current_app.logger.exception("Ошибка при сохранении ответа")
        return str(e), 500


@task.route("/submission/<int:submission_id>/grade", methods=["POST"])
def grade_submission(submission_id):
    sub = Submission.query.get_or_404(submission_id)
    try:
        g = request.form.get("grade")
        fb = request.form.get("feedback")
        sub.grade = int(g) if g else None
        sub.feedback = fb
        sub.graded = True
        db.session.commit()
        return redirect(url_for("main.teacher_home_check"))
    except Exception as e:
        db.session.rollback()
        current_app.logger.exception("Ошибка при выставлении оценки")
        return str(e), 500
