from imagine import app, db
from flask import render_template, request, redirect, url_for
from .forms import UserEmailForm, ContactForm
from .models import Email, Contact

@app.route('/', methods=['GET', 'POST'])
def search():
    form = UserEmailForm(request.form)
    # Add some sanitizing thing.
    if request.method == 'POST' and form.validate():
        db.session.add(Email(email=str(form.email.data)))
        db.session.commit()

        return render_template('index.html', success=True)
    return render_template('index.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	if request.method == 'POST' and form.validate():
		db.session.add(Contact(name=str(form.name.data), email=str(form.email.data), occupation=str(form.occupation.data), idea=str(form.idea.data), information=str(form.information.data)))
		db.session.commit()

		return render_template('index.html', success=True)
	return render_template('contact_us.html')