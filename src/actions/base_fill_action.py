import logging

from src.actions.base_find_locator_action import BaseFindLocator
from src.actions.base_wait_action import BaseWaitElement
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class BaseFillAction:
    context = "BaseFillAction"

    def __init__(self, page, locator: str):
        self.page = page
        self.locator = locator
        self.wait_element = BaseWaitElement(page=page, locator=self.locator)
        self.find_element = BaseFindLocator(page=page, locator=self.locator)

    @log_errors(context=f"{context}.fill_input_field", message="input text")
    def fill_input_field(self, text: str) -> None:
        """BaseFillAction.fill_input_field

                The method fills in a simple text or textarea field.
        """

        self.wait_element.wait_for_element()
        self.find_element.find_element_by_locator().fill(value=str(text))
