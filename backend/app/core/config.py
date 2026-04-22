import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "AegisOps AI"
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

settings = Settings()
