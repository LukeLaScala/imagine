from lhd import app, db
from flask import render_template, request, redirect, url_for
from .forms import UserEditForm, UserSearchForm, LaptopRegisterForm
from .models import User
WORKSHOPS = ['Minecraft Mods', 'Python', 'Web Dev', 'Arduino', 'Scratch', 'Games']
FIRST   =  [0, 3, 2, 1]
SECOND  =  [4, 0, 2, 1]
THIRD   =  [4, 3, 0, 1]
FOURTH  =  [4, 3, 2, 0]

@app.route('/', methods=['GET', 'POST'])
def search():
    form = UserSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        users = User.query.filter(User.last_name.like('%' + form.search.data + '%')).all()
        
        return render_template('search-results.html', users=users, query=form.search.data, form2=UserSearchForm())
    return render_template('register.html', form=form)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return str(sessionNumbers(1))

@app.route('/lookup/<id>/l4pt0p5', methods=['GET', 'POST'])
def laptop_info(id):
	user = User.query.filter_by(id=id).first()

	if request.method == 'POST':
		form = LaptopRegisterForm(request.form)
	else:
		form = LaptopRegisterForm(obj=user)

	if request.method == 'POST' and form.validate():
		form.populate_obj(user)
		user.laptop_out = form.laptop_out
		user.laptop_id = form.laptop_id
		print(form.laptop_out)
		print(form.laptop_id)
		db.session.commit()
		return redirect(url_for('laptop_info', id=user.id))

	return render_template('laptop-register.html', form=form,
	form2=LaptopRegisterForm(), user=user)

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
        slot1 = ""
        slot2 = ""
        slot3 = ""
        slot4 = ""

        requested = form.workshops.data
        
        ws1 = sessionNumbers(requested[0])
        ws2 = sessionNumbers(requested[1])
        ws3 = sessionNumbers(requested[2])

        best = 100000
        best1 = 100000
        best2 = 100000
        best3 = 100000

        for x in range(4):
        	for y in range(4):
        		for z in range(4):
        			if (ws1[x] != 100000) and (ws2[y] != 100000) and (ws3[y] != 100000):
        				total = int(ws1[x]) + int(ws2[y]) + int(ws3[z])
        				if total < best:
        					if x != y and x != z and y != z:
        						best1 = x
        						best2 = y
        						best3 = z
        						best = total

        if best1 == 0:
        	slot1 = requested[0]

        if best1 == 1:
        	slot2 = requested[0]

        if best1 == 2:
        	slot3 = requested[0]

        if best1 == 3:
        	slot4 = requested[0]


        if best2 == 0:
        	slot1 = requested[1]

        if best2 == 1:
        	slot2 = requested[1]
        
        if best2 == 2:
        	slot3 = requested[1]
        
        if best2 == 3:
        	slot4 = requested[1]
        


        if best3 == 0:
        	slot1 = requested[2]

        if best3 == 1:
        	slot2 = requested[2]
        
        if best3 == 2:
        	slot3 = requested[2]
        
        if best3 == 3:
        	slot4 = requested[2]

        if slot1 == "":
        	slot1 = 5
        if slot2 == "":
        	slot2 = 5
        if slot3 == "":
        	slot3 = 5
        if slot4 == "":
        	slot4 = 5

        #return "Slot 1: " + str(slot1)
        #return str(ws1) + '<br>' + str(ws2) + '<br>' + str(ws3) + '<br><br>' + "best1 : " + str(best1) + "best2: " + str(best2) + "best3: " + str(best3)



        form.populate_obj(user)
        user.slot1 = slot1
        user.slot2 = slot2
        user.slot3 = slot3
        user.slot4 = slot4
        db.session.commit()

        return redirect(url_for('lookup_user', id=user.id))
    
    userworkshops = str(user.slot1) + str(user.slot2) + str(user.slot3) + str(user.slot4)
    mine = '0' in userworkshops
    python = '1' in userworkshops
    web = '2' in userworkshops
    arduino = '3' in userworkshops
    scratch = '4' in userworkshops
    slot1 = "N/A"
    slot2 = "N/A"
    slot3 = "N/A"
    slot4 = "N/A"
    if user.slot1 or user.slot1 == 0:
    	slot1=WORKSHOPS[user.slot1]
    if user.slot2 or user.slot2 == 0:
    	slot2=WORKSHOPS[user.slot2]
    if user.slot3 or user.slot3 == 0:
    	slot3=WORKSHOPS[user.slot3]
    if user.slot4 or user.slot4 == 0:
    	slot4=WORKSHOPS[user.slot4]

    return render_template('edit.html', form=form,
     form2=UserSearchForm(), user=user, mine=mine, 
     python=python, web=web, arduino=arduino, scratch=scratch, 
     slot1=slot1, slot2=slot2, 
     slot3=slot3, slot4=slot4)

def sessionNumbers(sessNum):
	first, second, third, fourth = 100000, 100000, 100000, 100000

	if sessNum in FIRST:
		first = len(User.query.filter_by(slot1=sessNum).all())
		if first > 24:
			first = 100000
	if sessNum in SECOND:
		second = len(User.query.filter_by(slot2=sessNum).all())
		if second > 24:
			second = 100000
	if sessNum in THIRD:
		third = len(User.query.filter_by(slot3=sessNum).all())
		if third > 24:
			third = 100000	
	if sessNum in FOURTH:
		fourth = len(User.query.filter_by(slot4=sessNum).all())
		if fourth > 24:
			fourth = 100000

	return [first, second, third, fourth]
