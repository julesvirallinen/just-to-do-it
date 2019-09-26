from application import app
import arrow
from datetime import datetime, date



@app.template_filter()
def humanise(date):
    if not date: return ""
    return arrow.get(date).humanize()

@app.template_filter()
def style_task(task):
    style = ""
    if task.done:
        style = "list-group-item-success"
    elif task.deadline and task.deadline < datetime.today():
            style = "list-group-item-danger"
    return style

@app.template_filter()
def format_date(d):
    if d:
        return d.strftime('%Y-%m-%d')
    else:
        return "No deadline"


@app.template_filter()
def style_overdue(n):
    if n == 0:
        return "success"
    else:
        return "danger"
