import logging

from playwright.sync_api import expect
from src.actions.base_find_locator_action import BaseFindLocator
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class IsElementVisible:
    context = "IsElementVisible"
    
    def __init__(self, page, locator: str):
        self.page = page
        self.locator = locator
        self.find_element = BaseFindLocator(page=page, locator=self.locator)

    @log_errors(context=f"{context}.is_element_visible", message="visibility check")
    def is_element_visible(self) -> None:
        """IsElementVisible.is_element_visible

        This method check if the element is visible.

        """
        expect(self.find_element.find_element_by_locator()).to_be_visible(timeout=10000)

    @log_errors(context=f"{context}.is_element_not_visible", message="visibility check")
    def is_element_not_visible(self) -> None:
        """IsElementVisible.is_element_not_visible

        This method check if the element is not visible.

        """
        expect(self.find_element.find_element_by_locator()).not_to_be_visible(timeout=10000)
