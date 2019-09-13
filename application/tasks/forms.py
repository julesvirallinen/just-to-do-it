from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, DateField
from wtforms.fields.html5 import DateField

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=2)], render_kw={"placeholder": "Task name"})
    description = TextAreaField("Description", render_kw={"placeholder": "Description"})
    # deadline = DateField("Deadline", validators=(validators.Optional(),))

    class Meta:
        csrf = False
