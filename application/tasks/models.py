from application import db

from application.models import Base

from sqlalchemy.sql import text
1


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
    def find_tasks():
        stmt = text("SELECT Task.id, Task.name, Task.deadline, Task.category_id, Task.done FROM Task"
                    " LEFT JOIN Account ON Task.account_id = Account.id"
                    " WHERE Task.Category_id > 0"
                    " ORDER BY Task.done"
                    )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"id": row[0], "name": row[1], "deadline": row[2], "category": row[3], "done": row[4]})

        return response

    