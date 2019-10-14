from application import db
from datetime import datetime, date

from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user


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
        stmt = text("SELECT c.name, COUNT(t.category_id), c.id FROM Category c"
                    " LEFT JOIN Account a ON c.account_id = a.id"
                    " LEFT JOIN Task t ON c.id = t.category_id"
                    " AND (t.done = FALSE)"
                    " AND (t.possible_after IS NULL OR t.possible_after < to_date(cast(:today as TEXT),'YYYY-MM-DD'))"
                    " WHERE a.id = :current_account"
                    " GROUP BY c.name, c.id"
                    " ORDER BY c.id"

                    ).params(today=datetime.today(), current_account=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name": row[0], "count": row[1], "id": row[2]})
        # APPENDS COUNT FOR NULL CATEGORIES
        stmt = text("SELECT COUNT(t.id) FROM Task t"
                    " LEFT JOIN Account a ON t.account_id = a.id"
                    " WHERE(t.category_id IS NULL AND t.done=FALSE)"
                    " AND a.id = :current_account"
                    " AND (t.possible_after IS NULL OR t.possible_after < to_date(cast(:today as TEXT),'YYYY-MM-DD'))"

                    ).params(today=datetime.today(), current_account=current_user.id)
        res = db.engine.execute(stmt)

        for row in res:
            response.append(
                {"name": "No category", "count": row[0], "id": "none"})
        return response
