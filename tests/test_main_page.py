import time

from pages.base_page import BasePage


class TestMainPage:

    def test_driver_init(self, chrome):
        base = BasePage(chrome)

        base.get_page()


