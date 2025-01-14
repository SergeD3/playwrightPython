from allure import feature, title, step
from pages.login_page import LoginPage


class TestSuccessfulLogout:

    @feature("Authentication")
    @title("Проверяю что нажатие на кнопку Log out приводит к выходу из учётной записи")
    def test_log_out(self, authenticate_without_log_out):
        login_page = LoginPage(authenticate_without_log_out)

        with step("Нажимаю на кнопку Log out"):
            pass

        with step("Проверяю, что открыта страница login"):
            pass
