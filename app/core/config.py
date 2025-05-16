"""
Application configuration settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Awesome Project BE"
    DEBUG: bool = False
    # API_V1_STR: str = "/api/v1" # Ví dụ

    # Database Settings
    DATABASE_URL: str

    # Security Settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080 # 7 days

    # Celery Settings
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Email settings (tùy chọn, thêm nếu cần)
    # SMTP_TLS: bool = True
    # SMTP_PORT: Optional[int] = None
    # SMTP_HOST: Optional[str] = None
    # SMTP_USER: Optional[str] = None
    # SMTP_PASSWORD: Optional[str] = None
    # EMAILS_FROM_EMAIL: Optional[str] = None
    # EMAILS_FROM_NAME: Optional[str] = None
    # EMAILS_TO_SUPERUSER: Optional[str] = None # Ví dụ

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()
