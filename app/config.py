import os


class Config(object):
    USER = os.environ.get("POSTGRES_USEER", "admin")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD", "admin")
    HOST = os.environ.get("POSTGRES_HOST", "127.0.0.1")
    PORT = os.environ.get("POSTGRES_PORT", 5432)
    DB = os.environ.get("POSTGRES_DB", "mydb")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = "fb3hfb3ob4fuo3bdcqndeuwbfie3"
    SQLALCHEMY_TRACK_MODOFICATIONS = True
