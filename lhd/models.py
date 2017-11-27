from lhd import db, app
from datetime import datetime
from sqlalchemy.orm import backref

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    slot1 = db.Column(db.Integer)
    slot2 = db.Column(db.Integer)
    slot3 = db.Column(db.Integer)
    slot4 = db.Column(db.Integer)
    requested_laptop = db.Column(db.Boolean, default=False)
    received_laptop = db.Column(db.Boolean, default=False)
    returned_laptop = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.Unicode(256))
    last_name = db.Column(db.Unicode(256))
    is_registered = db.Column(db.Unicode(256))