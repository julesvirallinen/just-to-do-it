from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, DateField, Form, RadioField
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange
from dateutil.relativedelta import relativedelta
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.categories.models import Category


def year_ago():
    date = datetime.today() - relativedelta(years=1)
    return date.date


class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(
        min=2)], render_kw={"placeholder": "Task name"})
    description = TextAreaField("Description", render_kw={
                                "placeholder": "Description"})
    deadline = DateField(
        "Deadline",
        format='%Y-%m-%d',

        default=datetime.today,
        validators=[validators.Optional(),DateRange(min=(year_ago()))]
    )

    category = QuerySelectField("Category",
                                query_factory=lambda: Category.query.all(),
                                allow_blank=True,
                                blank_text='no category'
                                )

    class Meta:
        csrf = False
