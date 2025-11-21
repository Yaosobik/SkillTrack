from datetime import datetime
from app.extensions import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    task = db.Column(db.String(500))
    teacher = db.Column(db.String(100))
    student = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # ⁡⁢⁣⁢программа для миграции данных в БД: ⁡⁣⁢⁣𝗳𝗹𝗮𝘀𝗸 𝗱𝗯 𝗺𝗶𝗴𝗿𝗮𝘁𝗲⁡ ⁡⁢⁣⁢и⁡ ⁡⁣⁢⁣𝗳𝗹𝗮𝘀𝗸 𝗱𝗯 𝘂𝗽𝗴𝗿𝗮𝗱𝗲⁡
