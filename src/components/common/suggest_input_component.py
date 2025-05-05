import logging

from playwright.sync_api import Page, expect
from src.locators.common_locators import CommonLocators
from src.actions.base_click_action import BaseClick
from src.actions.base_fill_action import BaseFillAction
from src.actions.base_wait_action import BaseWaitElement
from src.actions.base_find_locator_action import BaseFindLocator
from src.pages.base_page import BasePage
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class SuggestInputComponent(BasePage):
    common_locators = CommonLocators()
    context = "SuggestInputComponent"

    def __init__(self, page: Page, locator: str):
        super().__init__(page)
        self.page = page
        self.locator = locator
        
        self.click_element = BaseClick(page=page, locator=self.locator)
        self.fill_suggest_input = BaseFillAction(page=page, locator=self.common_locators.SUGGEST_INPUT)
        self.find_suggest_input = BaseFindLocator(page=page, locator=self.common_locators.SUGGEST_INPUT)

    @log_errors(context=f"{context}.set_value_and_select", message="suggest input error")
    def set_value_and_select(self, value: str) -> None:
        logger.info("Set the value in the field")
        
        # click on the field
        
        self.click_element.click_on()
        
        # filling the field expected text
        
        self.fill_suggest_input.fill_input_field(text=value)
        
        # press 'Enter'
        
        self.find_suggest_input.find_element_by_locator().press("Enter")
        self.page.wait_for_timeout(1000)  # да простит меня дух машины за это
        
        # waiting for the value to be added to the field
        
        expect(self.find_suggest_input.find_element_by_locator()).to_have_value(value=value, timeout=10000)
        
        # select suggest item
        
        self.select_item(value=value)

    @log_errors(context=f"{context}.select_item", message="select item error")
    def select_item(self, value: str) -> None:
        logger.info("Choose the item from the list")

        new_locator = self.format_locator(locator=self.common_locators.SUGGEST_ITEM, text=value)
        suggest_item = BaseWaitElement(page=self.page, locator=new_locator)
        suggest_item_click = BaseClick(page=self.page, locator=new_locator)

        suggest_item.wait_for_element()
        suggest_item_click.click_on()
