import os
from dotenv import load_dotenv

load_dotenv()

DSN = os.getenv("DSN")
TOKEN_BOT = os.getenv("TOKEN_BOT")
TOKEN_API_VK = os.getenv("TOKEN_API_VK")
VERSION_API_VK = os.getenv("VERSION_API_VK")