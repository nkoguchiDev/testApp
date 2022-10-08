from pydantic import BaseSettings


class Settings(BaseSettings):

    # project settings
    PROJECT_NAME: str = "sns"
    API_V1_STR: str = "/api/v1"

    # datastore settings
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str = 'test'
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8


settings = Settings()
