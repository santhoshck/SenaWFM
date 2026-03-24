import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker  # type: ignore
from sqlalchemy.orm import declarative_base  # type: ignore

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/senawfm")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
