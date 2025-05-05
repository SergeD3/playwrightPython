import logging

from playwright.sync_api import expect, Page
from src.actions.base_find_locator_action import BaseFindLocator
from src.actions.base_wait_action import BaseWaitElement
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class IsElementContainsText:
    context = "IsElementContainsText"
    
    def __init__(self, page: Page, locator: str):
        self.page = page
        self.locator = locator
        self.find_element = BaseFindLocator(page=page, locator=self.locator)
        self.wait_element = BaseWaitElement(page=page, locator=self.locator)

    @log_errors(context=f"{context}.is_input_contains_value", message="checking input value")
    def is_input_contains_value(self, expected_value: str) -> None:
        expect(self.find_element.find_element_by_locator()).to_have_value(
            value=str(expected_value),
            timeout=10000
        )

    @log_errors(context=f"{context}.is_element_contains_text", message="checking element text")
    def is_element_contains_text(self, expected_text: str) -> None:
        expect(self.find_element.find_element_by_locator()).to_have_text(
            expected=str(expected_text),
            use_inner_text=True,
            timeout=10000
        )

    @log_errors(context=f"{context}.is_select_contains_option", message="checking selected option")
    def is_select_contains_option(self, expected_option: str) -> None:
        self.page.get_attribute(selector=self.locator, name=expected_option)

    @log_errors(context=f"{context}.is_checkbox_checked", message="checking checkbox state")
    def is_checkbox_checked(self, expected_state: bool) -> None:
        """IsElementContainsText.is_checkbox_checked

        Method checks whether element is checked or not.

        Parameters
        ----------
            expected_state : str
                The expected state of the checkbox.
        """
        expect(self.find_element.find_element_by_locator()).to_be_checked(checked=expected_state)
