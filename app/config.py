from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password: str
    database_username: str = "postgres"
    secret_key: str = "234kjdSdfiwr"


settings = Settings()
