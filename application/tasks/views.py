from datetime import datetime

from flask import redirect, render_template, request, url_for, flash, session
from flask_login import login_required, current_user
from sqlalchemy import desc, asc


from application import app, db
from application.tasks.models import Task
from application.categories.models import Category
from application.tasks.forms import TaskForm


@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    categories = Category.get_categories()
    tasks = Task.query.filter_by(account_id = current_user.id)

    if 'category' not in session:
        session['category'] = "all"

    if request.args.get('category'):
        session['category'] = request.args.get('category')

    category = session['category']
    
    if category != "all":
        if category == "none":
            category = None
        tasks = tasks.filter_by(category_id=category)

    tasks = tasks.order_by(Task.done, asc(Task.deadline)).all()        


    overdue = Task.count_overdue()[0]
    
    return render_template("tasks/index.html", tasks = tasks,
                           categories = categories,
                           overdue = overdue)


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
    cat = session['category']
    form = TaskForm()    
    if cat != "none" and cat != "all":
        form.category.default = Category.query.get(cat)
    form.process()
    return render_template("tasks/new.html", form = form)

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    dl = form.deadline.data
    pa = form.possible_after.data
    t = Task(form.name.data, form.description.data, dl, pa)
    t.account_id = current_user.id
    if(form.category.data):
        t.category_id = form.category.data.id


    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route('/task/edit/<task_id>', methods=['GET', 'POST'])
@login_required
def edit(task_id):

    task = Task.query.get(task_id)

    if task:
        if task.account_id != current_user.id:
            return redirect('/tasks')
        form = TaskForm(formdata=request.form, obj=task)
        if request.method == 'POST' and form.validate():
            task.deadline = form.deadline.data
            task.possible_after = form.possible_after.data

            task.name = form.name.data
            task.description = form.description.data
            if form.category.data:
                task.category_id = form.category.data.id
            
            db.session().commit()
            flash('Task updated successfully')

            return redirect('/tasks')

        return render_template('tasks/edit.html', form=form)
    else:
        return 'Error loading #{task_id}'.format(id=id)

@app.route('/task/del/<task_id>', methods=['POST'])
@login_required
def remove_task(task_id):

    task = Task.query.get(task_id)

    if task:
        if task.account_id != current_user.id:
            return redirect('/tasks')

        db.session().delete(task)
        db.session().commit()
        flash('Task removed successfully')

        return redirect('/tasks')

    else:
        return 'Error removing #{task_id}'.format(id=id)
