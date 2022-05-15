import email
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo,DataRequired,ValidationError,Email
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,PasswordField

class LoginForm (FlaskForm):
    email = StringField('Please enter your Email',validators=[DataRequired(),Email()])
    password = PasswordField('Please enter your Password',validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Log In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Enter your Username',validators=[DataRequired()])
    email = StringField('Please Enter Your Email',validators=[DataRequired(),Email()])
    password = PasswordField('Please Enter Your Password',validators=[DataRequired()])
    confirm_password = PasswordField('Please Retype Your Password',validators=[DataRequired(),EqualTo('confirm_password',message='Passwords do not match !')])
    submit = SubmitField('Sign Up')