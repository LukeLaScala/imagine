from flask_wtf import Form
from wtforms import Form, StringField

class UserEmailForm(Form):
    email = StringField('email')