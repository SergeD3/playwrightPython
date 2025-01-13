import re
import allure

from playwright.sync_api import Page, expect
from helpers import common_helper


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def goto_page(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def find_element_by(
            self,
            locator: str = None,
            loc_has_text: str = None,
            test_id: str = None,
            text: str = None,
            title: str = None
    ):
        if locator:
            return self.page.locator(selector=locator, has_text=loc_has_text)
        elif test_id:
            return self.page.get_by_test_id(test_id)
        elif text:
            return self.page.get_by_text(text)
        elif title:
            self.page.get_by_title(text=title)

    def find_element_by_role(self, role: str, name: str = None):
        return self.page.get_by_role(role=role, name=name)

    def left_click_on_element(self, test_id=None, locator=None):
        if test_id:
            self.find_element_by(test_id=test_id).click()
        elif locator:
            self.find_element_by(locator=locator).click()
        else:
            print("Необходимо указать test_id или locator")

    def fill_the_field(self, locator=None, test_id=None, text: str = ""):
        if locator:
            self.find_element_by(locator=locator).fill(text)
        elif test_id:
            self.find_element_by(test_id=test_id).fill(text)
        else:
            print("Необходимо указать locator или test_id")

    def get_text_from_element(self, locator=None, test_id=None):
        if locator:
            return self.find_element_by(locator=locator).inner_text()
        elif test_id:
            return self.find_element_by(test_id=test_id).inner_text()
        else:
            print("Необходимо указать locator или test_id")

    def get_element_attribute(self, attr, locator=None, test_id=None):
        if locator:
            return self.find_element_by(locator=locator).get_attribute(name=attr)
        elif test_id:
            return self.find_element_by(test_id=test_id).get_attribute(name=attr)
        else:
            print("Необходимо указать locator или test_id")

    def take_screenshot(self, step_name):

        allure.attach(
            self.page.screenshot(
                full_page=True
            ),
            name=step_name,
            attachment_type=allure.attachment_type.PNG
        )

    def take_element_screenshot(self, locator: str = None):
        name = helper.get_screenshot_date()

        self.find_element_by(locator=locator).screenshot(path=f"screenshots/{name}-element.jpeg")

    @staticmethod
    def is_match_url(current_url, expected_url):
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
