from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CheckboxState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    press_time = db.Column(db.DateTime, nullable=False)
    bool_state = None