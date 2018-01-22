from flask_wtf import Form
from wtforms import Form, StringField
from validate_email import validate_email

class UserEmailForm(Form):
    email = StringField('email')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        if not validate_email(str(self.email.data)):
            self.email.errors.append('Invalid Email')
            return False

        return True
class ContactForm(Form):
    name = StringField()
    email = StringField()
    occupation = StringField()
    idea = StringField()
    information = StringField()
    