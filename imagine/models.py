from imagine import db, app

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(256))

class Contact(db.Model):
	__tablename__ = "contacts"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(256))
	email = db.Column(db.Unicode(256))
	occupation = db.Column(db.Unicode(256))
	idea = db.Column(db.Unicode(1024))
	information = db.Column(db.Unicode(1024))
