import traceback

import allure
import logging

from playwright.sync_api import Page

logger = logging.getLogger(__name__)


def page_screenshot(page: Page):
    logger.info("Taking screenshot of the page")

    try:
        allure.attach(
            page.screenshot(
                full_page=True
            ),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:
        var = traceback.format_exc()
        
        logger.exception(f"Failed to take screenshot: {type(e).__name__} - {e}")
        logger.exception(var)

        raise e


def element_screenshot(page: Page, locator: str):
    logger.info("Taking screenshot of the element")
    
    try:
        allure.attach(
            page.locator(selector=locator).screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    
    except Exception as e:
        var = traceback.format_exc()

        logger.exception(f"Failed to take screenshot: {type(e).__name__} - {e}")
        logger.exception(var)

        raise e
