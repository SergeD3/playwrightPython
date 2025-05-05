import os
from dotenv import load_dotenv


load_dotenv()

BASE_URL: str = os.getenv('BASE_URL')
HTTP_PROTOCOL: str = os.getenv('HTTP_PROTOCOL')
ROBOT_USERNAME: str = os.getenv('ROBOT_USERNAME')
ROBOT_PASSWORD: str = os.getenv('ROBOT_PASSWORD')
ROBOT_NAME: str = os.getenv('ROBOT_NAME')
HEADLESS: str = os.getenv('HEADLESS')
PROJECT_NAME: str = os.getenv('PROJECT_NAME')
