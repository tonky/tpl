from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy  # type: ignore


db = SQLAlchemy()  # type: SQLAlchemy


class Load(db.Model):
    id = db.Column(db.String, primary_key=True)

    def __init__(self):
        self.id = uuid()

    def to_dict(self):
        return {'load_id': self.id}


def uuid():
    return str(uuid4())
