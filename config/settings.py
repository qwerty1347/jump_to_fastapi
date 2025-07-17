from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PORT: int
    MONGO_DB_PORT: int

    LOG_PATH: str
    UPLOAD_PATH: str

    CLOVA_OCR_SECRET_KEY: str
    CLOVA_OCR_APIGW_INVOKE_URL: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()