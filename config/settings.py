from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_URL: str
    
    # MySQL 설정
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    # MongoDB 설정
    MONGO_DB_PORT: int

    LOG_PATH: str
    UPLOAD_PATH: str

    # OCR
    CLOVA_OCR_SECRET_KEY: str
    CLOVA_OCR_APIGW_INVOKE_URL: str

    # JWT
    PYBO_JWT_EXPIRE_MINUTES: int
    PYBO_JWT_SECRET_KEY: str
    PYBO_JWT_ALGORITHM: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()