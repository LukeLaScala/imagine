from imagine import db, app

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(256))