from flask import Blueprint, render_template
from ..models.task import Task

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("main.html")


@main.route("/sign")
def sign():
    return render_template("sign.html")


@main.route("/sign/student")
def sign_student():
    return render_template("sign_student.html")


@main.route("/sign/teacher")
def sign_teacher():
    return render_template("sign_teacher.html")


@main.route("/registration")
def registration():
    return render_template("registr.html")


@main.route("/registration/student")
def registration_student():
    return render_template("registr_student.html")


@main.route("/registration/teacher")
def registration_teacher():
    return render_template("registr_teacher.html")


@main.route("/home/student")
def grades():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template("home_student.html", tasks=tasks)


@main.route("/home/teacher/check")
def teacher_home_check():
    # ленивый импорт модели Submission, чтобы избежать проблем при импортах
    from ..models.submission import Submission

    submissions = Submission.query.order_by(Submission.submitted_at.desc()).all()
    return render_template("home_teacher_check_tasks.html", submissions=submissions)


@main.route("/home/teacher/create")
def teacher_create():
    return render_template("home_teacher_send_task.html")


@main.route("/home/teacher/grades")
def teacher_grades():
    return render_template("home_teacher_grades.html")
