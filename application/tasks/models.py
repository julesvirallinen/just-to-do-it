from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)
    # deadline = db.column(db.DateTime)

    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.deadline = False
        self.done = False
