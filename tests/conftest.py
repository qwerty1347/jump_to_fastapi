import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

TEST_DB_URL = "mysql+aiomysql://root:root@127.0.0.1:3306/fastapi?charset=utf8mb4"

engine_test = create_async_engine(TEST_DB_URL, echo=True)
AsyncSessionLocalTest = sessionmaker(
    engine_test, class_=AsyncSession, expire_on_commit=False
)

@pytest_asyncio.fixture
async def db() -> AsyncSession:
    async with AsyncSessionLocalTest() as session:
        yield session
        await session.rollback()
