from flask import Blueprint
from ..extensions import db
from ..models.user import Student, Teacher

student = Blueprint("student", __name__)
teacher = Blueprint("teacher", __name__)


@student.route("/student/<name>")
def create_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return "Студент успешно зарегестрирован!"


@teacher.route("/teacher/<name>")
def create_teacher(name):
    teacher = Teacher(name=name)
    db.session.add(teacher)
    db.session.commit()
    return "Преподаватель успешно зарегестрирован!"
