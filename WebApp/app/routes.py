from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, forms, utils
from app.models import Hospital, Info
from datetime import datetime

# *****************************************************************************
# *                                  ROUTES                                   *
# *****************************************************************************


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    info = Info.query.all()[-1]
    if request.method == 'POST':
        data = request.get_json()
        utils.print_to_stderr(data)


        newInfo = Info(hospital=info.hospital,
                       time=datetime.now(),
                       total_num_beds=info.total_num_beds,
                       used_num_beds=info.used_num_beds,
                       total_num_vent=info.total_num_vent,
                       used_num_vent=info.used_num_vent,
                       num_adm=info.num_adm,
                       used_dis=info.used_dis)

        if data['chosenOperation'] == "Add":
            newInfo.add(data['chosenResource'], data['requestedAmount'])
        elif data['chosenOperation'] == "Remove":
            newInfo.remove(data['chosenResource'], data['requestedAmount'])
        elif data['chosenOperation'] == "Patient(s) In":
            newInfo.patient_in(data['chosenResource'], data['requestedAmount'])
        elif data['chosenOperation'] == "Patient(s) Out":
            newInfo.patient_out(data['chosenResource'], data['requestedAmount'])
        utils.print_to_stderr(newInfo)
        db.session.add(newInfo)
        db.session.commit()
        return data
    else:
        utils.print_to_stderr(info)
        data = {
            'availBeds': info.total_num_beds - info.used_num_beds,
            'totalBeds': info.total_num_beds,
            'totalVents': info.total_num_vent,
            'availVents': info.total_num_vent - info.used_num_vent
        }
        return jsonify(data)

@app.route('/edit-info', methods=['GET', 'POST'])
def edit_info():
    return render_template('edit_info.html')


@app.route('/hospitals', methods=['GET'])
def hospitals():
    return render_template('tracker/hospitals.html')


@app.route('/testGraphs', methods=['GET'])
def testGraphs():
    return render_template('testGraphs.html')


# *****************************************************************************
# *                               User Handling                               *
# *****************************************************************************


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = forms.LoginForm()
    if form.validate_on_submit():
        hospital = Hospital.query.filter_by(username=form.username.data).first()

        if hospital is None or not hospital.check_password(form.password.data):
            flash("Invalid username or password")

        login_user(hospital, remember=form.remember.data)

        return redirect(url_for('index'))

    return render_template('auth/login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = forms.RegistrationForm()

    if form.validate_on_submit():
        hospital = Hospital(username=form.username.data, hospital_name=form.hospital_name.data)
        hospital.set_password(form.password.data)
        db.session.add(hospital)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('auth/register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
