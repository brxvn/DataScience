from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={"placeholder": "Username"}, label="Username", )
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Password"}, label="Password")
    submit = SubmitField("Login")


class Todoform(FlaskForm):
    description = StringField(validators=[DataRequired()], render_kw={"placeholder": "Description"}, label="Description")
    submint = SubmitField("Add")


class DeleteTodoForm(FlaskForm):
    submint = SubmitField("Delete")


class UpdateTodoForm(FlaskForm):
    submint = SubmitField("Update")