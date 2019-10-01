from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class UserForm(FlaskForm):
    username = StringField("Username",
        [validators.Length(min=2, max=50)])
    password = PasswordField("Password",
        [validators.Length(min=4, max=50)])


    class Meta:
        csrf = False
