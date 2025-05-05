from allure import step
from src.pages.menu.menu_page import MenuPage
from src.utils.env import BASE_URL
from src.locators.login_page_locators import LoginPageLocators
from src.pages.base_page import BasePage
from src.actions.base_click_action import BaseClick
from src.actions.base_fill_action import BaseFillAction


class LoginPage(BasePage):
    BASE_PATH = "#/Login"

    def __init__(self, page):
        super().__init__(page)
        self.login_page_loc = LoginPageLocators()
        self.menu_page = MenuPage(page)

        self.login_btn = BaseClick(page=page, locator=self.login_page_loc.LOGIN_BTN)
        self.logout_menu_item = BaseClick(page=page, locator=self.menu_page.logout_menu_item.menu_item)
        self.username_input = BaseFillAction(page=page, locator=self.login_page_loc.USERNAME_INP)
        self.password_input = BaseFillAction(page=page, locator=self.login_page_loc.PASSWORD_INP)

    @step("Перехожу на страницу login")
    def get_login_page(self):
        self.goto_page(f"https://{BASE_URL}/{self.BASE_PATH}")

    @step("Заполняю поле username")
    def fill_username(self, username):
        self.username_input.fill_input_field(text=username)

    @step("Заполняю поле password")
    def fill_password(self, password):
        self.password_input.fill_input_field(text=password)

    @step("Нажимаю кнопку Log in")
    def click_login_button(self):
        self.login_btn.click_on()

    @step("Заполняю поля email, password и нажимаю кнопку Log in")
    def fill_form_fields_and_click_on_log_in(self, username: str, password: str):
        with step("Filling 'Username'"):
            self.fill_username(username)

        with step("Filling 'Password'"):
            self.fill_password(password)

        with step("Click on log in"):
            self.click_login_button()

    @step("Log out")
    def click_logout(self):
        self.menu_page.user_icon_menu.click_on_menu_item()
        self.logout_menu_item.click_on()

    @step("Проверяю, что страница login открыта")
    def is_login_page_open(self):
        self.expect(self.find_element(by_locator=self.login_page_loc.LOGO_LOGIN_PAGE)).to_be_visible()
        self.take_screenshot()

    @step("Проверяю, что отображается ошибка о том что логин или пароль некорректные")
    def is_err_alert_present(self):
        expected_text = 'Login credentials incorrect, please try again.'

        self.expect(
            self.find_element(by_locator=self.login_page_loc.WRONG_CREDS_ALERT)
        ).to_contain_text(
            expected=expected_text,
            use_inner_text=True,
            timeout=10000
        )

        self.take_screenshot()
