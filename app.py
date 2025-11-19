from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskonline.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship('Student', back_populates='group')


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', back_populates='students')
    # связь с выполниными заданиями
    assignments = db.relationship('Assignment', back_populates='student')


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    assignments = db.relationship('Assignment', back_populates='teacher')


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher', back_populates='assignments')


class StudentAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    assignment_id = db.relationship(db.Integer, db.ForeignKey('assignment.id'))
    answer_text = db.Column(db.Text)
    grade = db.Column(db.Integer)
    student = db.relationship('Student', back_populates='assignments')
    assignment = db.relationship('Assignment', back_populates='student')
@app.route('/')
def index():
    return render_template('Main.html')


if __name__ == '__main__':
    app.run(debug=True)

