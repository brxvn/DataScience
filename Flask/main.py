import unittest
from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from unittest import TextTestRunner

app = Flask(__name__)
app.config["ENV"] = "development"
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "thisisasecret"

bootstrap = Bootstrap(app)

todos = ["Comprar café", "Enviar solicitud de compra", "Entregar video a productor"]


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={"placeholder": "Username"}, label="Username", )
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Password"}, label="Password")
    submit = SubmitField("Login")


@app.cli.command()
def test():
    test = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session["user_ip"] = user_ip
    return response


@app.route("/hello", methods=["GET", "POST"])
def hello():
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get("username")

    context = {"user_ip": user_ip, 
               "todos": todos,
               "login_form": login_form,
               "username": username}

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash("Nombre de usuario registrado con éxito")
        return redirect(url_for("index"))
    
    return render_template("hello.html", **context)

if __name__ == "__main__":
    app.run()