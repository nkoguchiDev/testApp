from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str = 'test'
    SECRET_KEY = "cce45e4c8450c2781ff1f2e1436cd61fb49c730f5b74b7b4824ca09d77eb89c3"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8


settings = Settings()
