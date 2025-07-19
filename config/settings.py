from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    MONGO_DB_PORT: int

    LOG_PATH: str
    UPLOAD_PATH: str

    CLOVA_OCR_SECRET_KEY: str
    CLOVA_OCR_APIGW_INVOKE_URL: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()