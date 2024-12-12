import data

from pages.base_page import BasePage
from playwright.sync_api import sync_playwright


class LoginPage(BasePage):

    def get_login_page(self):
        self.get_page(data.LOGIN_PAGE)

    def is_login_page_opened(self):
        return self.expect(self.page).to_have_url(data.LOGIN_PAGE)
