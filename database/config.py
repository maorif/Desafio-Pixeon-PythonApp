from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql+asyncpg://postgres:123456@postgres/fastAPI_app_db"
database_engine = create_async_engine(database_url)
database_async_session = sessionmaker(bind=database_engine, class_=AsyncSession)
