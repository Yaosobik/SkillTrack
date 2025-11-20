from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
db = SQLAlchemy(app)


class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/home")
def grades():
    return render_template("home_student.html")


@app.route("/sign")
def sign_in():
    return render_template("sign.html")


@app.route("/registration")
def registration():
    return render_template("registr.html")


@app.route("/thome")
def teacher_home():
    return render_template("home_teacher.html")


if __name__ == "__main__":
    app.run(debug=True)
