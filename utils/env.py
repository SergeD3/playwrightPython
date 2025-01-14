import os
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()
    return {
        'BASE_URL': os.getenv('BASE_URL'),
        'ROBOT_USERNAME': os.getenv('ROBOT_USERNAME'),
        'ROBOT_PASSWORD': os.getenv('ROBOT_PASSWORD'),
        'ROBOT_NAME': os.getenv('ROBOT_NAME'),
        'HEADLESS': os.getenv('HEADLESS')
    }
