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
    elif task.possible_after and task.possible_after > datetime.today():
            style = "disabled"
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
    
@app.template_filter()
def format_possible(n):
    if n and n > datetime.today():
        return "Available " + arrow.get(n).humanize()
    else:
        return ""

@app.template_filter()
def count_all(cat):
    sum = 0;
    for c in cat:
        sum += c['count']
    return sum
