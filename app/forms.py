from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   username = StringField("Name",validators=[DataRequired()])
   password = PasswordField("Password",validators=[DataRequired()])
   remember_me = BooleanField("Remember?")
   submit=SubmitField("SignIn")

class RegisterForm(FlaskForm):
   username = StringField("Name",validators=[DataRequired()])
   password = PasswordField("Password",validators=[DataRequired()])
   repass = PasswordField("Re-Type",validators=[DataRequired()])

