from flask_wtf import Form
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, SelectField, HiddenField, validators, SelectMultipleField

class UserEditForm(Form):
    id = HiddenField('id')
    laptop_out = BooleanField('Laptop Out')
    laptop_id = StringField('Laptop Id')
    workshops = SelectMultipleField(coerce=int, choices=[(0, 'Minecraft Mods'), (1, 'Python'), (2, 'Web Dev'), (3, 'Arduino'), (4, 'Scratch')])

class UserSearchForm(Form):
    search = StringField('search', [validators.DataRequired()])
