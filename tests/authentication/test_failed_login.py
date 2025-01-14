from pytest import mark
from pages.login_page import LoginPage
from allure import title, feature, step


class TestFailedLogin:

    @feature("Authentication")
    @title("Проверяю, что при вводе невалидного логина или пароля попытка авторизоваться возвращает ошибку")
    @mark.parametrize('username, password', [])
    def test_login_page_invalid_credentials(self, page, username, password):
        username = username
        password = password

        login_page = LoginPage(page)
        main_page = None

        with step("Открываю главную страницу"):
            pass

        with step("Нажимаю кнопку Sign in (Войти)"):
            pass

        with step("Заполняю поля на форме и затем нажимаю кнопку Log in"):
            pass

        with step("Проверяю, что появился предупреждение, что логин или пароль неверные"):
            pass

        with step("Проверяю, что пользователь не был перенаправлен на другую страницу"):
            pass
