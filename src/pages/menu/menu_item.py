from allure import step
from src.actions.base_click_action import BaseClick


class MenuItem:

    def __init__(self, page, locator):
        self.menu_item = locator
        self.click_on_item = BaseClick(page=page, locator=self.menu_item, log_name=__name__)

    @step("Click on the menu item")
    def click_on_menu_item(self):
        self.click_on_item.click_on()
