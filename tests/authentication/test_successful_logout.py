import allure

from pages.login_page import LoginPage


class TestSuccessfulLogout:

    @allure.feature("Authentication")
    @allure.title("Проверяю что нажатие на кнопку Log out приводит к выходу из учётной записи")
    def test_log_out(self, authenticate_without_log_out):
        login_page = LoginPage(authenticate_without_log_out)

        with allure.step("Нажимаю на кнопку Log out"):
            pass

        with allure.step("Проверяю, что открыта страница login"):
            pass
