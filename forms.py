from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
# from wtforms.validators import DataRequired

class SignupForm(FlaskForm):
    """docstring for SignupForm."""
    first_name = StringField('First Name',[validators.Length(min=3, max=100)])
    last_name = StringField('Last Name',[
        validators.DataRequired("Please enter your last name")
    ])
    email = StringField('Email',[
        validators.DataRequired("Your email please"),
        validators.Email("Valid email please")
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', [
        validators.DataRequired("Your email please"),
        validators.Email("Valid email please")
    ])
    password = PasswordField('Password', [
        validators.DataRequired("Please provide password")
    ])
    submit = SubmitField('Sign in')

class AddressForm(FlaskForm):
    address = StringField('Address',[
        validators.DataRequired("Please enter address: ")
    ])
    submit = SubmitField('Search')
