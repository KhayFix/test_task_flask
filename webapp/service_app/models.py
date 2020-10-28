from webapp.db import db
from datetime import datetime


class CheckboxState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    press_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    bool_state = db.Column(db.Boolean)

    def __repr__(self):
        return f"{self.bool_state} - {self.press_time}"
