from allure import title, feature, step
from pytest import mark
from src.pages.login.login_page import LoginPage
from src.pages.home.home_page import HomePage
from src.utils.env import ROBOT_USERNAME, ROBOT_PASSWORD


class TestSuccessfulLogin:

    @feature("Authentication")
    @title("После успешной авторизации отображается страница проекта")
    @mark.smoke
    @mark.tryfirst
    def test_login_page_valid_credentials(self, log_out):
        username = ROBOT_USERNAME
        password = ROBOT_PASSWORD

        login_page = LoginPage(log_out)
        home_page = HomePage(log_out)

        with step("Открываю главную страницу Web"):
            login_page.get_login_page()

        with step(f"Заполняю поля username: {username} и пароль: {password}, затем нажимаю кнопку Log in"):
            login_page.fill_form_fields_and_click_on_log_in(username=username, password=password)

        with step("Проверяю, что открылась страница mail box"):
            home_page.is_home_page_opened()
