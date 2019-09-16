from flask import render_template, redirect
from application import app

@app.route("/")
def index():
    return redirect("/tasks")
