from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, DateField, Form
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange
from dateutil.relativedelta import relativedelta

def year_ago():
    date = datetime.today() - relativedelta(years=1)
    return date.date

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)], render_kw={"placeholder": "Task name"})
    description = TextAreaField("Description", render_kw={"placeholder": "Description"})
    deadline = DateField(
        "Deadline",
        format='%Y-%m-%d',

        default=datetime.today,
        validators=[DateRange(min=(year_ago()))]
    )

    class Meta:
        csrf = False


