import re
import allure

from playwright.sync_api import Page, expect
from src.helpers import common_helper as helper


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def goto_page(self, url: str):
        self.page.goto(url=url)

    def get_current_url(self):
        return self.page.url

    def find_element(
            self,
            by_locator: str = None,
            loc_has_text: str = None,
            test_id: str = None,
            text: str = None,
            title: str = None
    ):
        if by_locator:
            return self.page.locator(selector=by_locator, has_text=loc_has_text).first
        elif test_id:
            return self.page.get_by_test_id(test_id)
        elif text:
            return self.page.get_by_text(text)
        elif title:
            self.page.get_by_title(text=title)

    def find_element_by_role(
            self,
            role: str = None,
            name: str = None
    ):
        return self.page.get_by_role(role=role, name=name)

    def left_click_on_element(
            self,
            test_id: str = None,
            locator: str = None
    ):
        if locator:
            self.find_element(by_locator=locator).click()
        else:
            self.find_element(test_id=test_id).click()

    def fill_the_field(
            self,
            locator: str = None,
            test_id: str = None,
            text: str = ""
    ):
        if locator:
            self.page.wait_for_selector(selector=locator)
            self.find_element(by_locator=locator).fill(text)
        else:
            self.find_element(test_id=test_id).fill(text)

    def get_text_from_element(
            self,
            locator=None,
            test_id=None
    ):
        if locator:
            return self.find_element(by_locator=locator).inner_text()
        else:
            return self.find_element(test_id=test_id).inner_text()

    def get_element_attribute(
            self,
            attr: str,
            locator: str = None,
            test_id: str = None
    ):
        if locator:
            return self.find_element(by_locator=locator).get_attribute(name=attr)
        else:
            return self.find_element(test_id=test_id).get_attribute(name=attr)

    @staticmethod
    def format_locator(locator: str, text: str):
        result = locator.format(text=text)

        return result

    def take_screenshot(self):
        allure.attach(
            self.page.screenshot(
                full_page=True
            ),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    def take_element_screenshot(self, locator: str = None):
        name = helper.get_screenshot_date()

        self.find_element(by_locator=locator).screenshot(path=f"screenshots/{name}-element.jpeg")

    @staticmethod
    def is_match_url(
            current_url: str = "",
            expected_url: str = ""
    ):
        """
        Проверяет, что ожидаемый URL частично или полностью входит в текущий URL.

        :param current_url: Текущий URL.
        :param expected_url: Ожидаемый URL.
        :return: True, если ожидаемый URL частично или полностью входит в текущий URL, иначе False.
        """
        # Экранируем специальные символы в ожидаемом URL для использования в регулярном выражении
        escaped_expected_url = re.escape(expected_url)

        # Создаем регулярное выражение, которое проверяет наличие ожидаемого URL в текущем URL
        pattern = re.compile(escaped_expected_url)
        result: bool = bool(pattern.search(current_url))

        if result:
            return result
        else:
            print(f"Ошибка: {pattern=} - {current_url=}")

    # методы для управления страницей браузера

    def refresh_page(self):
        self.page.reload()
