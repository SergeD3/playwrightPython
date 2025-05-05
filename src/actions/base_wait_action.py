import logging

from playwright.sync_api import Page, ElementHandle
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class BaseWaitElement:
    context = "BaseWaitElement"

    def __init__(self, page: Page, locator: str):
        self.page = page
        self.locator = locator

    @log_errors(context=f"{context}.wait_for_element", message="wait element")
    def wait_for_element(self) -> ElementHandle | None:
        self.page.wait_for_selector(selector=self.locator)

    @log_errors(context=f"{context}.wait_until_page_loads", message="wait element")
    def wait_until_page_loads(self):
        self.page.wait_for_load_state(state="domcontentloaded")
