from datetime import datetime

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user


from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm


@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())


@app.route("/task/<task_id>", methods=["GET"])
@login_required
def get_task(task_id):
    return render_template("tasks/task.html", task = Task.query.get(task_id))


@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.done:
        t.done = False
    else:
        t.done = True
    db.session().commit()

    return redirect(url_for("tasks_index"))


@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    dl = form.deadline.data
    t = Task(form.name.data, form.description.data, dl)
    t.account_id = current_user.id

    # t.deadline =

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route('/task/edit/<task_id>', methods=['GET', 'POST'])
def edit(task_id):

    task = Task.query.get(task_id)

    if task:
        form = TaskForm(formdata=request.form, obj=task)
        if request.method == 'POST' and form.validate():
            task.deadline = form.deadline.data
            task.name = form.name.data
            task.description = form.description.data
            db.session().commit()
            flash('Task updated successfully')

            return redirect('/tasks')

        return render_template('tasks/edit.html', form=form)
    else:
        return 'Error loading #{task_id}'.format(id=id)
