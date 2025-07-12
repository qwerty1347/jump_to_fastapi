from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PORT: int
    MONGO_DB_PORT: int

    LOG_PATH: str
    UPLOAD_PATH: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()