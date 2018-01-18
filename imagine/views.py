from imagine import app, db
from flask import render_template, request, redirect, url_for
from .forms import UserEmailForm
from .models import Email

@app.route('/', methods=['GET', 'POST'])
def search():
    form = UserEmailForm(request.form)
    # Add some sanitizing thing.
    if request.method == 'POST' and form.validate():
        db.session.add(Email(email=form.email.data))
        db.session.commit()
        # Do I need to include an error checker thing?  To make sure that it's added successfully?
        return render_template('success.html')
    return render_template('index.html', form=form)