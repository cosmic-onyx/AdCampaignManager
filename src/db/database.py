from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db.config import settings


async_engine = create_async_engine(
    url=settings.get_db_url,
    echo=True,
)

async_session = async_sessionmaker(async_engine)


async def in_db_session(stmt, method=None):
    async with async_session() as session:
        res = await session.execute(stmt)

        if method is None:
            await session.commit()

        await session.close()
        return res