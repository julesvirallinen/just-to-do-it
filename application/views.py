from flask import render_template, redirect
from application import app
from flask_login import current_user

@app.route("/")
def index():
    if current_user:
        return redirect("/tasks")
    else:
        return redirect("/auth/login")
