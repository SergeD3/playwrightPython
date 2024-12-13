import allure

import data as dt
import pytest

from pages.login_page import LoginPage


class TestLoginPage:

    @allure.title("После успешной авторизации отображается страница проекта")
    def test_login_page_valid_credentials(self, chrome):
        username = dt.ROBOT_USERNAME
        password = dt.ROBOT_PASSWORD

        login_page = LoginPage(chrome)

        login_page.get_login_page()
        login_page.is_login_page_opened()
        login_page.fill_form_fields(username=username, password=password)
        login_page.click_login_button()

        login_page.expect(login_page.page).to_have_url(f"{dt.BASE_URL}/#project")

    @allure.title("Проверяю, что при вводе невалидного логина или пароля попытка авторизоваться возвращает ошибку")
    @pytest.mark.parametrize('username, password', [
        {"wrong_username", dt.ROBOT_PASSWORD},
        {dt.ROBOT_USERNAME, "wrong_password1245"},
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
