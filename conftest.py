import shutil
import logging
import traceback

import pytest
import os

from allure import step, title
from playwright.sync_api import sync_playwright
from src.helpers.auth_helper import AuthHelper
from src.helpers.delete_record_helper import DeleteRecordHelper
from src.utils.env import HEADLESS
from os import path, makedirs

logger = logging.getLogger(__name__)


@pytest.fixture
def chrome():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=lambda HEADLESS: True if HEADLESS == 'yes' else False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        page.close()
        browser.close()


@pytest.fixture(params=['chrome'])
def page(request):
    screen_resolution: dict = {'width': 1366, 'height': 728}
    headless_mode: bool = True if HEADLESS == 'yes' else False

    with step(f"Launching browser: {request.param}"):
        logger.info(f"Launching browser: {request.param}")

        with sync_playwright() as p:
            try:
                if request.param == 'chrome':
                    browser = p.chromium.launch(headless=headless_mode)
                elif request.param == 'firefox':
                    browser = p.firefox.launch(headless=headless_mode)
                else:
                    raise ValueError(f"Unsupported browser: {request.param}")

                context = browser.new_context(viewport=screen_resolution)
                page = context.new_page()

                yield page

            except Exception as e:
                logger.exception(f"{type(e)} Browser launch error: {e}")
            finally:
                page.close()
                browser.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Определяем корневую директорию проекта
    rootdir = config.rootdir

    # Указываем путь к логам относительно корневой директории
    log_file = os.path.join(rootdir, "logs", "pytest.log")

    # Создаём директорию для логов, если её нет
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Устанавливаем путь к логам
    config.option.log_file = log_file


@title("Clear allure_results folder")
@pytest.fixture(scope="session", autouse=True)
def clear_allure_results():
    allure_results_dir = 'allure_results'

    logger.info("Clearing allure_results folder")
    try:
        if path.exists(allure_results_dir):
            shutil.rmtree(allure_results_dir)
            
        makedirs(allure_results_dir)

    except Exception as e:
        var = traceback.format_exc()
        
        logger.exception(f"{type(e)} Clear allure_results folder error: {e}")
        logger.exception(var)
        
        raise e


@title("authentication with logging out")
@pytest.fixture
def authenticated_session(page):
    with step("Вход в учётную запись"):
        auth = AuthHelper(page)
        auth.authentication()

        yield page

        auth.log_out()


@title("authentication without logging out")
@pytest.fixture
def authenticate_without_log_out(page):
    auth = AuthHelper(page)
    auth.authentication()

    yield page


@title("Logging out")
@pytest.fixture
def log_out(page):
    yield page

    log_out = AuthHelper(page)
    log_out.log_out()


@title("Deleting record")
@pytest.fixture
def delete_record():
    def _delete(page, url: str, module_path: str):
        delete_entity = DeleteRecordHelper(page=page)

        delete_entity.delete_record(url=url, module_path=module_path)

    return _delete
