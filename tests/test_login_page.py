import allure
import data as dt
import pytest
import os

from pages.login_page import LoginPage


class TestLoginPage:

    @allure.title("После успешной авторизации отображается страница проекта")
    def test_login_page_valid_credentials(self, chrome):
        username = os.getenv('ROBOT_USERNAME')
        password = os.getenv('ROBOT_PASSWORD')
        login_page = LoginPage(chrome)

        login_page.get_login_page()
        login_page.is_login_page_opened()
        login_page.fill_form_fields(username=username, password=password)
        login_page.click_login_button()

        login_page.is_authorization_successful()

    @allure.title("Проверяю, что при вводе невалидного логина или пароля попытка авторизоваться возвращает ошибку")
    @pytest.mark.parametrize('username, password', [
        {"wrong_username", os.getenv('ROBOT_PASSWORD')},
        {os.getenv('ROBOT_USERNAME'), "wrong_password1245"},
    ])
    def test_login_page_invalid_credentials(self, chrome, username, password):
        username = username
        password = password
        login_page = LoginPage(chrome)

        login_page.get_login_page()
        login_page.is_login_page_opened()
        login_page.fill_form_fields(username=username, password=password)
        login_page.click_login_button()

        login_page.is_err_alert_present()
