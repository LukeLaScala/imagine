from lhd import app, db
from flask import render_template, request, redirect, url_for
from .forms import UserEmailForm
from .models import Email

@app.route('/', methods=['GET', 'POST'])
def search():
    email = UserEmailForm(request.form)
    # Add some sanitizing thing.
    if request.method == 'POST' and form.validate():
        db.session.add(email)
        db.session.commit()
        # Do I need to include an error checker thing?  To make sure that it's added successfully?
        return render_template('temp2.html', users=users, query=form.search.data, form2=UserSearchForm())
    return render_template('temp.html', form=form)