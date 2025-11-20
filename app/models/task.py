from app.extensions import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    task = db.Column(db.String(500))
