from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, DateField, Form
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange
from dateutil.relativedelta import relativedelta



class CategoryForm(FlaskForm):
    name = StringField("Category name", 
                       [validators.Length(min=2, max=50)], 
                       render_kw={"placeholder": "Category name"})

    class Meta:
        csrf = False


