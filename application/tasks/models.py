from application import db

from application.models import Base

from sqlalchemy.sql import text
from datetime import datetime, date


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

    @staticmethod
    def count_overdue():
        stmt = text("SELECT COUNT(Task.id) FROM Task"
                    " LEFT JOIN Account ON Task.account_id = Account.id"
                    " WHERE (Task.deadline < to_date(cast(:today as TEXT),'YYYY-MM-DD'))"
                    " AND Task.done = FALSE"
                    
                    ).params(today=datetime.today())
        res = db.engine.execute(stmt)
        print(res)
        response = []
        for row in res:
            response.append(
                row[0])
        print(response)

        return response

    