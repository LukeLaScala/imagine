from lhd import db, app

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    slot1 = db.Column(db.Integer, nullable=True)
    slot2 = db.Column(db.Integer, nullable=True)
    slot3 = db.Column(db.Integer, nullable=True)
    slot4 = db.Column(db.Integer, nullable=True)
    laptop_out = db.Column(db.Boolean, default=False)
    laptop_id = db.Column(db.Unicode(256), nullable=True)
    first_name = db.Column(db.Unicode(256))
    last_name = db.Column(db.Unicode(256))
    school = db.Column(db.Unicode(256))