from sqlalchemy import select, insert, update, delete, and_

from db.database import in_db_session


class BaseRepository:
    def __init__(self):
        self.model = None

    def _build_conditions(self, filters):
        conditions = []
        for key, value in filters.items():
            conditions.append(getattr(self.model, key) == value)

        return conditions

    async def insert_one(self, values):
        stmt = insert(self.model).values(values)
        return await in_db_session(stmt)

    async def update_one(self, filters, values):
        stmt = update(self.model).where(
            and_(*self._build_conditions(filters))
        ).values(values)
        return await in_db_session(stmt)

    async def find_one(self, filters):
        stmt = select(self.model).where(
            and_(*self._build_conditions(filters))
        )
        return await in_db_session(stmt, 'get')

    async def delete_one(self, filters):
        stmt = delete(self.model).where(
            and_(*self._build_conditions(filters))
        )
        return await in_db_session(stmt)

    async def find(self, filters=None):
        if filters is None:
            filters = {}

        stmt = select(self.model).where(
            and_(*self._build_conditions(filters))
        )
        return await in_db_session(stmt, 'get')