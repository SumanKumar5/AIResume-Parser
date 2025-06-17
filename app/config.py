from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME: str = "AIResume Parser"
    API_VERSION: str = "v1"

settings = Settings()
