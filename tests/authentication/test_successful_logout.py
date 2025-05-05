from allure import feature, title, step
from src.pages.login.login_page import LoginPage
from pytest import mark


class TestSuccessfulLogout:

    @feature("Authentication")
    @title("Проверяю что нажатие на кнопку Log out приводит к выходу из учётной записи")
    @mark.smoke
    def test_log_out(self, authenticate_without_log_out):
        login_page = LoginPage(authenticate_without_log_out)

        with step("Нажимаю на кнопку Log out"):
            login_page.click_logout()

        with step("Проверяю, что открыта страница login"):
            login_page.is_login_page_open()
