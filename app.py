from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskonline.db'
db = SQLAlchemy(app)


#БД ученика
class Discipl (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Teacher (db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    return render_template('Main.html')


if __name__ == '__main__':
    app.run(debug=True)

