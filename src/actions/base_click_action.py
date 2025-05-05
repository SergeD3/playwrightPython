import logging

from src.actions.base_find_locator_action import BaseFindLocator
from playwright.sync_api import Page
from src.utils.logging import log_errors


class BaseClick:
    context = "BaseClick"

    def __init__(self, page: Page, locator: str, log_name: str = __name__):
        self.page = page
        self.locator = locator
        self.logger = logging.getLogger(log_name)
        
        self.find_element = BaseFindLocator(page=page, locator=self.locator)

    @log_errors(context=f"{context}.click_on", message="click on element")
    def click_on(self, button: str = "left") -> None:
        """BaseClick.click_on

        Click an element.

        Parameters
        ----------
        button : str
            press the 'left', 'right' or 'middle' button.
            'left' button by default.

        """

        self.find_element.find_element_by_locator().click(button=button)

    @log_errors(context=f"{context}.set_checkbox_state", message="set checkbox state")
    def set_checkbox_state(self, checkbox_state: bool = True) -> None:
        """BaseClick.set_checked

        Set the state of a checkbox or a radio element.
        'True' by default.

        Parameters
        ----------
        checkbox_state:
            Whether to check or uncheck the checkbox.
        """

        self.find_element.find_element_by_locator().set_checked(checked=checkbox_state)
