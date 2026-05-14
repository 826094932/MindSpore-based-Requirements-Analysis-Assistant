from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "SmartPM MindSpore AI Demo"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "sk-a91b6b36177b48889e4b16697e3b7304")
    DEEPSEEK_BASE_URL: str = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    USE_MOCK: bool = os.getenv("USE_MOCK", "False").lower() == "true"
    
    class Config:
        env_file = ".env"

settings = Settings()
