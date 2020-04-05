from flask_wtf import FlaskForm
from app.models import Hospital, Info
from wtforms import StringField, HiddenField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField, \
    SelectField, Form
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Hospital ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Hospital ID', validators=[DataRequired()])
    hospital_name = StringField('Hospital Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Hospital.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username")

    def validate_email(self, email):
        user = Hospital.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address")
