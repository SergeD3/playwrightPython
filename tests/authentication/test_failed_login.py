from pytest import mark

from src.pages.login.login_page import LoginPage
from allure import title, feature, step
from src.utils.env import ROBOT_USERNAME, ROBOT_PASSWORD


class TestFailedLogin:

    @feature("Authentication")
    @title("Проверяю, что при вводе невалидного логина или пароля попытка авторизоваться возвращает ошибку")
    @mark.smoke
    @mark.parametrize('username, password', [
        ["wrong_username", ROBOT_PASSWORD],
        [ROBOT_USERNAME, "wrong_password1245"],
    ])
    def test_login_page_invalid_credentials(self, page, username, password):
        login_page = LoginPage(page)

        with step("Открываю главную страницу Web"):
            login_page.get_login_page()

        with step(f"Заполняю поля email: {username} и пароль: {password}, затем нажимаю кнопку Log in"):
            login_page.fill_form_fields_and_click_on_log_in(username=username, password=password)

        with step("Проверяю, что появился предупреждение, что логин или пароль неверные"):
            login_page.is_err_alert_present()

        with step("Проверяю, что пользователь не был перенаправлен на другую страницу"):
            login_page.is_login_page_open()
