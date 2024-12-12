import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture
def chrome():
    with sync_playwright() as p:
        # инициализация браузера (без видимого открытия браузера)
        # browser = p.chromium.launch()

        # инициализация браузера (с явным открытием браузера)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()
