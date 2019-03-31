from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField,SelectField,FileField,TextAreaField
from wtforms.validators import InputRequired,Email,DataRequired
from flask_wtf.file import FileRequired,FileAllowed
from wtforms.widgets import TextArea

class ProfileForm(Form):
    first_name = StringField('First Name', validators=[DataRequired('Your first name is required!')])
    last_name = StringField('Last Name', validators=[DataRequired('Your Last name is required!')])
    gender = SelectField(u'Gender', choices=[('Select','Select Gender'),('M', 'Male'), ('F', 'Female'), ('O', 'Other')], validators = [InputRequired()])
    email = StringField('Email Address', validators=[DataRequired('An email address is required!'), Email('Please enter an appropriate email address.')], render_kw={"placeholder": "e.g. youremailaddress@default.com"})
    location = StringField('Location', validators=[DataRequired('Your location is required!')], render_kw={"placeholder": "e.g. Spanish Town, Jamaica"})
    biography = TextAreaField('Biography', validators=[DataRequired('A message is required!')])
    image = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])