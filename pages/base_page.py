import data

from playwright.sync_api import Page, expect

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect
        self.main_page = MainPageLocators()
        self.login_page = LoginPageLocators()

    def get_page(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def find_element_by_locator(self, locator: str):
        element = self.page.locator(locator)

        return element

    def find_element_by_test_id(self, test_id: str):
        element = self.page.get_by_test_id(test_id)

        return element

    def left_click_on_button(self, test_id=None, locator=None):
        if test_id:
            element = self.find_element_by_test_id(test_id)
            element.click()
        elif locator:
            element = self.find_element_by_locator(locator)
            element.click()
        else:
            print("Необходимо указать test_id или locator")


