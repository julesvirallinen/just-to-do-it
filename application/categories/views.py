from datetime import datetime

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user


from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm



@app.route("/categories/new/")
@login_required
def category_form():
    return render_template("categories/new.html", form = CategoryForm())


@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form = form)

    t = Category(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/categories/")
@login_required
def category_list():
    categories = Category.get_categories()
    print(categories)
    return render_template("categories/index.html", categories=categories)

@app.route('/category/del/<category_id>', methods=['POST'])
def remove_category(category_id):

    category = Category.query.get(category_id)

    if category:
        for task in category.tasks:
            task.category_id = None
            db.session().commit()
            
        db.session().delete(category)
        db.session().commit()
        flash('Category removed successfully')

        return redirect('/categories')

    else:
        return 'Error removing #{category_id}'.format(id=id)

