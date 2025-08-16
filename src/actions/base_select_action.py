import logging

from src.actions.base_find_locator_action import BaseFindLocator
from src.actions.base_wait_action import BaseWaitElement
from playwright.sync_api import Page
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class BaseSelectOption:
    context = "BaseSelectOption"

    def __init__(self, page: Page, locator: str):
        self.locator = locator
        self.wait_element = BaseWaitElement(page=page, locator=self.locator)
        self.find_element = BaseFindLocator(page=page, locator=self.locator)

    @log_errors(context=f"{context}.select_option", message="select option")
    def select_option(self, value: str = None, index: int = None) -> list[str]:
        """BaseSelectOption.select_option

        Select the option.

        Parameters
        ----------
        value : str
            Options to select by value.
        index: int
            Options to select by index.

        """

        self.wait_element.wait_for_element()

        if value:
            return self.find_element.find_element_by_locator().select_option(value=value)
        else:
            return self.find_element.find_element_by_locator().select_option(index=index)
