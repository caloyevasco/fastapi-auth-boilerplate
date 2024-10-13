from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    MONGO_DB_URI: str
    DATABASE_NAME: str

    ACCESS_TOKEN_DURATION: int
    REFRESH_TOKEN_DURATION: int


settings = Settings()
