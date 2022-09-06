import os
from dotenv import load_dotenv

load_dotenv()

DSN = os.getenv("DSN")
TOKEN_BOT = os.getenv("TOKEN_BOT")
TOKEN_API_VK = os.getenv("TOKEN_API_VK")
GROUP_ID = os.getenv("GROUP_ID")
VERSION_API_VK = os.getenv("VERSION_API_VK")

LOGIN_DB = os.getenv("LOGIN_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")