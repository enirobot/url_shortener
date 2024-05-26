from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    BASE_URL: str = "http://localhost:9999"
    SHORT_URL_LENGTH: int = 5
    URL_EXPIRATION_DAYS: int = 30
    SHORT_KEY_RETRIES: int = 5

    class Config:
        env_file = ".env"


settings = Settings()
