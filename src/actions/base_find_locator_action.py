import logging

from playwright.sync_api import Locator, Page
from src.actions.base_wait_action import BaseWaitElement
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class BaseFindLocator:
    context = "FindElementByLocator"

    def __init__(self, page: Page, locator: str):
        self.page = page
        self.locator = locator
        self.wait_element = BaseWaitElement(page=page, locator=self.locator)

    @log_errors(context=f"{context}.find_element_by_locator", message="find element")
    def find_element_by_locator(self) -> Locator:
        """BaseFindLocator.find_element_by_locator

        This method allows to find an element by xpath or css.
        """
        self.wait_element.wait_for_element()

        return self.page.locator(selector=self.locator).first
