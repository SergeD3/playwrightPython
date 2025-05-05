import logging

from src.locators.common_locators import CommonLocators
from src.locators.opportunities.opportunity_page_locators import OpportunityPageLocators
from src.actions.base_click_action import BaseClick
from playwright.sync_api import Page
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class CalendarInputComponent:
    context = "CalendarInputComponent"
    common_locators = CommonLocators()
    opportunities_loc = OpportunityPageLocators()

    def __init__(self, page: Page, locator: str):
        self.page = page
        self.locator = locator
        self.click_element = BaseClick(page=page, locator=self.locator)

    @log_errors(context=f"{context}.set_current_date", message="set date error")
    def set_current_date(self):
        logger.info("Setting the date")

        choose_date = BaseClick(page=self.page, locator=self.opportunities_loc.CALENDAR_DATE)

        # actions

        self.click_element.click_on()
        choose_date.click_on()
