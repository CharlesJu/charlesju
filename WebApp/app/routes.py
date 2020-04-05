from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, forms, utils
from app.models import Hospital, Info


# *****************************************************************************
# *                                  ROUTES                                   *
# *****************************************************************************


@app.route('/')
@app.route('/index')
# @login_required
def index():
    if request.method == 'POST':
        data = request.get_json()

        utils.print_to_stderr(data)
        return jsonify(data)
    # return jsonify("")

    # return redirect(url_for('testGraphs'))
    return render_template('tracker/index.html', title='index')


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
