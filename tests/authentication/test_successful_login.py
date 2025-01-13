# import os

from allure import title, feature, step
from pages.login_page import LoginPage


class TestSuccessfulLogin:

    @feature("Authentication")
    @title("После успешной авторизации отображается страница проекта")
    def test_login_page_valid_credentials(self, log_out):
        username = None
        password = None

        login_page = LoginPage(log_out)

        with step("Открываю страницу login"):
            pass

        with step("Нажимаю кнопку Sign in (Войти)"):
            pass

        with step("Заполняю поля на форме и затем нажимаю кнопку Log in"):
            pass

        with step("Проверяю, что аутентификация прошла успешно"):
            pass
