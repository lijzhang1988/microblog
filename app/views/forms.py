from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,FileField
from wtforms.validators import DataRequired,Length


class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])


class EditForm(FlaskForm):
    nickname=StringField(label='Nickname',validators=[DataRequired(message='nickname is required.')])
    description=TextAreaField(label='About Me',validators=[Length(min=0,max=140)])
    image=FileField(label='Image')


class NewUserForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(message='username is required.')])
    password = PasswordField(label='Password',validators=[DataRequired(message='password is required.')])
    nickname = StringField(label='Nickname',validators=[DataRequired(message='nickname is required.')])
    description = TextAreaField(label='About Me',validators=[Length(min=0,max=140)])


