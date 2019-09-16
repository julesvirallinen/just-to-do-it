from application import app
import arrow


@app.template_filter()
def humanise(text):
    
    return arrow.get(text).humanize()
