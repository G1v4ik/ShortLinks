from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = 'local',
    base_url: str = 'http://127.0.0.1:8000'
    db_url: str = 'sqlite:///./links.db'

    class Config:
        env_file = ".env"
    

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings