from pydantic import BaseSettings, Field
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Settings(BaseSettings):
    """
    Configuration settings for the AI Wrapper MVP.

    This class defines application-wide settings, including database connection details, API endpoints, logging configuration, and other parameters. 

    Environment Variables:
        - `OPENAI_API_KEY`: The API key for accessing OpenAI's API. 
        - `DATABASE_URL`: The connection string for the PostgreSQL database.
        - `LOG_LEVEL`: The logging level to use (e.g., "INFO", "DEBUG").
        - `LOG_FILE`: The path to the log file for storing logging information. 

    """

    APP_NAME: str = Field("OpenAI-Query-Wrapper-MVP", env="APP_NAME")
    APP_VERSION: str = Field("1.0.0", env="APP_VERSION")
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    DATABASE_URL: Optional[str] = Field("postgresql://user:password@host:port/database", env="DATABASE_URL")
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")
    LOG_FILE: str = Field("app.log", env="LOG_FILE")
    JWT_SECRET_KEY: str = Field("your_secret_key", env="JWT_SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()