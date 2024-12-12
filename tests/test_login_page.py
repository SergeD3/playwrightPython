from pages.login_page import LoginPage


class TestLoginPage:

    def test_login_page(self, chrome):
        login_page = LoginPage(chrome)

        login_page.get_login_page()
        assert login_page.is_login_page_opened()
