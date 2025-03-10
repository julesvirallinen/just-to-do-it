from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")



    login_user(user, remember=True)
    flash('Logged in successfully.')

    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("auth/registration.html", form = LoginForm())

    form = UserForm(request.form)

    if not form.validate():
        return render_template("/auth/registration.html", form = form,
                               error = "Username must be between 2 and 50 characters and password must be between 4 and 50 characters.")

    u = User(form.username.data, form.password.data)
    if User.query.filter_by(username=form.username.data).first():
        return render_template("/auth/registration.html", form = form,
                                error = "Username taken, try again")

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("tasks_index"))




@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
