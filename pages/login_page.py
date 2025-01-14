from allure import step
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, chrome):
        super().__init__(chrome)
        self.lp_locators = LoginPageLocators()

    @step("Перехожу на страницу аутентификации")
    def get_login_page(self):
        pass

    @step("Проверяю, что страница аутентификации открыта")
    def is_login_page_opened(self):
        pass

    @step("Проверяю, что аутентификация пройдена успешно")
    def is_authentication_successful(self):
        pass

    @step("Заполняю поле логин")
    def fill_username(self, username):
        pass

    @step("Заполняю поле пароль")
    def fill_password(self, password):
        pass

    @step("Заполняю поля логин и пароль")
    def fill_form_fields(self, username, password):
        pass

    @step("Нажимаю кнопку Войти")
    def click_login_button(self):
        pass

    @step("Проверяю, что отображается всплывающее уведомление")
    def is_err_alert_present(self):
        pass
