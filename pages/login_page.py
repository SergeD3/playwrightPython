import data
import allure
import os

from dotenv import load_dotenv
from pages.base_page import BasePage


class LoginPage(BasePage):
    load_dotenv()

    def __init__(self, chrome):
        super().__init__(chrome)

    @allure.step("Перехожу на страницу аутентификации")
    def get_login_page(self):
        self.get_page(f"{os.getenv('BASE_URL')}{data.LOGIN_PAGE}")

    @allure.step("Проверяю, что страница аутентификации открыта")
    def is_login_page_opened(self):
        expected_url = f"{os.getenv('BASE_URL')}{data.LOGIN_PAGE}"

        self.expect(self.page).to_have_url(expected_url)

    def is_authorization_successful(self):
        expected_url = f"{os.getenv('BASE_URL')}{data.DASHBOARD_PAGE}"

        self.expect(self.page).to_have_url(expected_url)
        self.expect(self.find_element_by_locator(self.dashboard_page_locators.NO_WIDGETS_IMG)).to_be_visible()

    @allure.step("Заполняю поле логин")
    def fill_username(self, username):
        self.fill_the_field(test_id=self.login_page_locators.USERNAME_FIELD, text=username)

    @allure.step("Заполняю поле пароль")
    def fill_password(self, password):
        self.fill_the_field(test_id=self.login_page_locators.PASSWORD_FIELD, text=password)

    @allure.step("Заполняю поля логин и пароль")
    def fill_form_fields(self, username, password):
        self.fill_username(username)
        self.fill_password(password)

    @allure.step("Нажимаю кнопку Войти")
    def click_login_button(self):
        self.find_element_by_test_id(self.login_page_locators.LOGIN_BUTTON).click()

    @allure.step("Проверяю, что отображается всплывающее уведомление")
    def is_err_alert_present(self):
        expected_text = "Ошибка"

        element = self.find_element_by_locator(self.login_page_locators.ERROR_ALERT_MESSAGE)
        self.expect(element).to_have_text(expected=expected_text, use_inner_text=True)
