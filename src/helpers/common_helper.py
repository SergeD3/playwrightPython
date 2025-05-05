import random
import string
import json
import logging

from faker import Faker
from pathlib import Path
from datetime import datetime, date
from src.pages.accounts.schemas import Account
from pydantic import ValidationError


fake = Faker(locale='en')
current_file_path = Path(__file__).resolve()
project_root_path = current_file_path.parent.parent
logger = logging.getLogger(__name__)


def get_screenshot_date() -> str:
    current_date = datetime.now().strftime("%Y-%m-%d-%H%M%S")

    return f"-{current_date}-{random.randint(100, 99999)}"


def get_random_name(name_type: str = "individual") -> str:
    if name_type == "individual":
        return f"QA_AUTO {fake.name()}"
    else:
        return fake.company()


def get_random_last_name() -> str:
    return fake.last_name()


def get_city_name() -> str:
    return fake.city()


def get_random_website():
    return fake.url()


def get_random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def get_random_street() -> str:
    return fake.street_address()


def get_random_mobile_phone() -> str:
    return fake.basic_phone_number()


def get_phone_number() -> str:
    """
    Функция возвращает случайный номер телефона в формате +7XXXXXXXXXX.
    """
    random_digits = ''.join(random.choices('0123456789', k=10))
    phone_number = f"+7{random_digits}"

    return phone_number


def get_random_email() -> str:
    email = fake.email(domain='yandex.ru')

    return email


def get_random_id() -> str:
    return fake.uuid4()


def get_random_number(length: int = None) -> str:
    if length:
        return fake.random_number(digits=length, fix_len=True)
    else:
        return fake.random_number(digits=None, fix_len=False)


def get_current_date() -> dict:
    """
    Функция возвращает словарь с ключами day, month, year, full-date и соответствующие значения
    """

    now_date = {
        "day": date.today().day,
        "month": date.today().month,
        "year": date.today().year,
        "full-date": date.today().strftime("%d-%m-%Y")
    }

    return now_date


def get_test_data(module: str) -> list[dict]:
    """get_test_data

    This method returns test data from json file based on the passed test data file name.

    Parameters
    ----------
    module:
        module name
    """
    path_file = project_root_path / "test_data" / f"{module}.json"
    test_data_list: list = []

    entity_schema: dict = {
        "accounts": Account
    }

    try:
        with (open(path_file, mode='r', encoding='utf-8') as f):
            data = json.load(f)

            model = entity_schema.get(module)

            for key, value in data.items():
                account = model.model_validate(data[key][0])
                test_data_list.append(account)

        return test_data_list

    except ValidationError as e:
        logger.exception(f"Validation error: {e}")

        raise e

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")

        raise e


if __name__ == '__main__':
    pass
