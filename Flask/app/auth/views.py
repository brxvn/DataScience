from flask import render_template
from flask import render_template, session, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import UserData, UserModel
from . import auth
from app.forms import LoginForm
from app.firestore_service import get_user, add_user
from app.models import UserModel, UserData

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {"login_form": login_form}

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user_doc = get_user(username)

        if user_doc.to_dict() is not None:

            if check_password_hash(user_doc.to_dict()['password'], password):
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)
                flash("Bienvenido de nuevo")
                redirect(url_for('hello'))
            else:
                flash("La contraseña es incorrecta")
        else:
            flash("Credenciales invalidas")

        return redirect(url_for("index"))

    return render_template("login.html", **context)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    signup_form = LoginForm()
    context = {"signup_form": signup_form}

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            add_user(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash("Usuario creado exitosamente")
            return redirect(url_for("hello"))
        else:
            flash("El usuario ya existe")

    return render_template("signup.html", **context)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Adios")
    return redirect(url_for("auth.login"))