from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, DateField, Form
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange


class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)], render_kw={"placeholder": "Task name"})
    description = TextAreaField("Description", render_kw={"placeholder": "Description"})
    deadline = DateField(
        validators=[DateRange(min=date.today())]
    )

    class Meta:
        csrf = False
