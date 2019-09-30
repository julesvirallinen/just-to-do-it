from flask import render_template, redirect, url_for, request, session
from application import app
from flask_login import current_user

@app.route("/")
def index():
    if current_user:
        return redirect(url_for('tasks_index'))
    else:
        return redirect("/auth/login")
