from flask_wtf  import FlaskForm

from wtforms import StringField, HiddenField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField, SelectField, Form
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange

class LoginForm(FlaskForm):
  hospital_id = StringField('Hospital ID', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  hospital_id = StringField('Hospital ID', validators=[DataRequired()])
  hospital_name = StringField('Hospital Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired()])
  submit = SubmitField('Register')
