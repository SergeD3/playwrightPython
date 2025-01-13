import pytest
import os
import allure

from playwright.sync_api import sync_playwright
# from dotenv import load_dotenv

# load_dotenv()


@pytest.fixture
def chrome():
    with sync_playwright() as p:
        headless_mode: bool = True if os.getenv('HEADLESS') == "True" else False

        browser = p.chromium.launch(headless=headless_mode)
        context = browser.new_context()
        page = context.new_page()

        yield page

        page.close()
        browser.close()


@pytest.fixture(params=['chrome', 'firefox'])
def page(request):
    screen_resolution: dict = {'width': 1280, 'height': 1024}
    headless_mode: bool = True if os.getenv('HEADLESS') == "True" else False

    with allure.step(f"Запускаю браузер: {request.param}"):
        with sync_playwright() as p:
            if request.param == 'chrome':
                browser = p.chromium.launch(headless=headless_mode)
            elif request.param == 'firefox':
                browser = p.firefox.launch(headless=headless_mode)
            else:
                raise ValueError(f"Unsupported browser: {request.param}")

            context = browser.new_context(viewport=screen_resolution)
            page = context.new_page()

            yield page

            page.close()
            browser.close()
