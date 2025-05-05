import logging

from src.pages.home.home_page import HomePage
from src.pages.login.login_page import LoginPage
from allure import step
from src.utils.env import ROBOT_USERNAME, ROBOT_PASSWORD
from src.utils.logging import log_errors

logger = logging.getLogger(__name__)


class AuthHelper:
    contex = "AuthHelper"

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)

    @step("Authentication")
    @log_errors(context=f"{contex}.authentication", message="auth error")
    def authentication(self) -> None:
        logger.info(f"Authenticating user. Login: {ROBOT_USERNAME} / Password: {ROBOT_PASSWORD}")

        self.login_page.get_login_page()
        self.login_page.fill_form_fields_and_click_on_log_in(username=ROBOT_USERNAME, password=ROBOT_PASSWORD)
        self.home_page.is_home_page_opened()

    @step("logging out")
    @log_errors(context=f"{contex}.log_out", message="log out error")
    def log_out(self) -> None:
        logger.info("Logging out")

        self.login_page.click_logout()
        self.login_page.is_login_page_open()
