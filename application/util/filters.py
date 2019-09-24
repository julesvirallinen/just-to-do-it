from application import app
import arrow
from datetime import datetime, date



@app.template_filter()
def humanise(text):
    
    return arrow.get(text).humanize()

@app.template_filter()
def style_task(task):
    style = ""
    if task.done:
        style = "list-group-item-success"
    elif task.deadline < datetime.today():
        style = "list-group-item-danger"
    return style
