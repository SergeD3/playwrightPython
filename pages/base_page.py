import data

from playwright.sync_api import Page, expect

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect
        self.main_page_locators = MainPageLocators()
        self.login_page_locators = LoginPageLocators()

    def get_page(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def find_element_by_locator(self, locator: str):
        return self.page.locator(locator)

    def find_element_by_test_id(self, test_id: str):
        return self.page.get_by_test_id(test_id)

    def left_click_on_button(self, test_id=None, locator=None):
        if test_id:
            self.find_element_by_test_id(test_id).click()
        elif locator:
            self.find_element_by_locator(locator).click()
        else:
            print("Необходимо указать test_id или locator")

    def fill_the_field(self, locator=None, test_id=None, text: str = ""):
        if locator:
            self.find_element_by_locator(locator=locator).fill(text)
        elif test_id:
            self.find_element_by_test_id(test_id=test_id).fill(text)
        else:
            print("Необходимо указать locator или test_id")
