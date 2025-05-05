from allure import step
from src.pages.base_page import BasePage
from src.locators.home_page_locators import HomePageLocators
from src.utils.env import BASE_URL, HTTP_PROTOCOL


class HomePage(BasePage):
    HOME_PATH = "#/home"

    def __init__(self, page):
        super().__init__(page)
        self.home_page_loc = HomePageLocators()

    @step("Проверяю что открыта страница Home")
    def is_home_page_opened(self):
        self.page.wait_for_url(url=f"{HTTP_PROTOCOL}{BASE_URL}/{self.HOME_PATH}")
        self.expect(self.find_element(by_locator=self.home_page_loc.HOME_BTN)).to_be_visible()

        self.take_screenshot()
