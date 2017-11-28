from lhd import app, db
from flask import render_template, request, redirect, url_for
from .forms import UserEditForm, UserSearchForm
from .models import User

@app.route('/', methods=['GET', 'POST'])
def search():
    form = UserSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        users = User.query.filter(User.last_name.like('%' + form.search.data + '%')).all()
        
        return render_template('search-results.html', users=users, query=form.search.data)
    return render_template('register.html', form=form)

@app.route('/lookup/<id>', methods=['GET', 'POST'])
def lookup_user(id):
    user = User.query.filter_by(id=id).first()    
    
    if request.method == 'POST':
        form = UserEditForm(request.form)
    else:
        form = UserEditForm(obj=user)

    if request.method == 'POST' and form.validate():
        if len(form.workshops.data) != 3:
            return "Error, you must select 3 workshops"

        form.populate_obj(user)
        db.session.commit()

        return redirect(url_for('search'))
    userworkshops = str(user.slot1) + str(user.slot2) + str(user.slot3) + str(user.slot4)
    mine = '0' in userworkshops
    python = '1' in userworkshops
    web = '2' in userworkshops
    arduino = '3' in userworkshops
    scratch = '4' in userworkshops
    return render_template('edit.html', form=form, form2=UserSearchForm(), user=user, mine=mine, python=python, web=web, arduino=arduino, scratch=scratch)