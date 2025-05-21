from pydantic import BaseSettings, Field
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # Weaviate configuration
    WEAVIATE_URL: str = Field(..., env="WEAVIATE_URL")
    WEAVIATE_API_KEY: str | None = Field(None, env="WEAVIATE_API_KEY")

    # LLM configuration
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    LLM_MODEL: str = Field("gpt-4", env="LLM_MODEL")
    TEMPERATURE: float = Field(0.7, env="TEMPERATURE")
    MAX_TOKENS: int = Field(1024, env="MAX_TOKENS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
