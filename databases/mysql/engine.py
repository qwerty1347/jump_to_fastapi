from sqlalchemy.ext.asyncio import create_async_engine

from config.settings import settings


DATABASE_URL = (
    f"mysql+aiomysql://"
    f"{settings.DB_USERNAME}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/"
    f"{settings.DB_DATABASE}?charset=utf8mb4"
)

engine = create_async_engine(DATABASE_URL, echo=True)