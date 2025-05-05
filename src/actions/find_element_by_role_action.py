import logging

from playwright.sync_api import Locator, Page
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class FindElementByRole:
    context = "FindElementByRole"
    
    def __init__(self, page: Page, role_locator: tuple):
        self.page = page
        self.role, self.name = role_locator

    @log_errors(context=f"{context}.find_element_by_role", message="find element")
    def find_element_by_role(self) -> Locator:
        """FindElementByRole.find_element_by_role

        This method allows to find an element by role and name.
        """
        return self.page.get_by_role(
            role=self.role,
            name=self.name
        )
