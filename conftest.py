import pytest
import os

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def chrome():
    with sync_playwright() as p:
        headless_mode: bool = True if os.getenv('HEADLESS') == "True" else False

        # инициализация браузера (с явным открытием браузера)
        browser = p.chromium.launch(headless=headless_mode)
        context = browser.new_context()
        page = context.new_page()

        yield page

        page.close()
        browser.close()
