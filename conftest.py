import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture
def chrome():
    with sync_playwright() as p:
        # инициализация браузера (с явным открытием браузера)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        browser.close()
