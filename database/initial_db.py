from asyncio import run

from database.config import database_engine
from database.models import Base

async def create_database():
    async with database_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    run(create_database())