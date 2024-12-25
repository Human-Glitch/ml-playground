from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from loguru import logger
from sqlalchemy import create_engine

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="config/.env", env_file_encoding="utf-8")
    
    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_connection_string: str
    
settings = Settings()

logger.remove()
logger.add("logging/app.log", rotation="1 day", retention="2 days", compression="zip", level=settings.log_level)
engine = create_engine(settings.db_connection_string)