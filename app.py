from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"


@app.route("/")
def home():
    return render_template("main.html")



@app.route("/sign")
def sign_in():
    return render_template("sign.html")


@app.route("/sign/student")
def sign_student():
    return render_template("sign_student.html")


@app.route("/sign/teacher")
def sign_teacher():
    return render_template("sign_teacher.html")


@app.route("/registration")
def registration():
    return render_template("registr.html")


@app.route("/registration/student")
def registration_student():
    return render_template("registr_student.html")


@app.route("/registration/teacher")
def registration_teacher():
    return render_template("registr_teacher.html")


@app.route("/home/student")
def grades():
    return render_template("home_student.html")


@app.route("/home/teacher")
def teacher_home():
    return render_template("home_teacher.html")


if __name__ == "__main__":
    app.run(debug=True)
