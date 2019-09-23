from application import db

from application.models import Base

class Task(Base):


    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)
    deadline = db.Column(db.DateTime)

    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=True)


    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.done = False

    # def __repr__(self):
    #     return '<%r %r %r>' % ()

    