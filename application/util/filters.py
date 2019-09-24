from application import app
import arrow
from datetime import datetime, date


@app.template_filter()
def humanise(text):
    return arrow.get(text).humanize()

@app.template_filter()
def style_task(task):
    style = ""
    if task:
        style = "list-group-item-success list-task-done"
    # elif task[1] < datetime.today():
        # style = "list-group-item-danger"
    return style
