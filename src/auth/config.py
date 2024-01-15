import os

from dotenv import load_dotenv

load_dotenv()


MIN_USERNAME_LENGTH = os.environ.get("MIN_USERNAME_LENGTH")
MAX_USERNAME_LENGTH = os.environ.get("MAX_USERNAME_LENGTH")

MIN_PASSWORD_LENGTH = os.environ.get("MIN_PASSWORD_LENGTH")
MAX_PASSWORD_LENGTH = os.environ.get("MAX_PASSWORD_LENGTH")