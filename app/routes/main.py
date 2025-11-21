from flask import Blueprint, render_template

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
    return render_template("home_student.html")


@main.route("/home/teacher")
def teacher_home():
    return render_template("home_teacher.html")
