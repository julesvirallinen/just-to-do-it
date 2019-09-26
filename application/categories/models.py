from application import db

from application.models import Base
from sqlalchemy.sql import text


class Category(Base):

    name = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    tasks = db.relationship('Task', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @staticmethod
    def get_categories():
        stmt = text("SELECT c.name, COUNT(t.category_id) FROM Category c"
                    " LEFT JOIN Account a ON c.account_id = a.id"
                    " LEFT JOIN Task t ON c.id = t.category_id"
                    " WHERE ( t.done = FALSE)"
                    " GROUP BY c.name"
                    # " HAVING COUNT(Task.id) = 0"
                    )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name": row[0], "count": row[1]})
        #APPENDS COUNT FOR NULL CATEGORIES
        stmt = text("SELECT COUNT(t.id) FROM Task t"
            " LEFT JOIN Account a ON t.account_id = a.id"
            " WHERE (t.category_id IS NULL AND t.done = FALSE)"
            )
        res = db.engine.execute(stmt)
        
        for row in res:
            response.append({"name": "None", "count": row[0]})
        return response
