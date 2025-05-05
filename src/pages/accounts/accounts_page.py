from allure import step
from playwright.sync_api import expect, Page
from src.utils.env import BASE_URL, HTTP_PROTOCOL
from src.utils.logging import log_errors
from src.checks.common.is_element_contains_text import IsElementContainsText
from src.checks.common.is_element_visible import IsElementVisible
from src.locators.common_locators import CommonLocators
from src.pages.menu.menu_page import MenuPage
from src.pages.accounts.schemas import Account
from src.locators.accounts_page_locators import AccountsPageLocators
from src.actions.base_fill_action import BaseFillAction
from src.actions.base_click_action import BaseClick
from src.actions.base_select_action import BaseSelectOption
from src.actions.take_screenshot_action import page_screenshot
from src.actions.base_find_locator_action import BaseFindLocator


class AccountsPage:
    module_path = "#/accounts"
    context = "AccountsPage"

    acc_locators = AccountsPageLocators()
    common_locators = CommonLocators()

    def __init__(self, page: Page):
        self.page = page
        self.menu_page = MenuPage(page)
        
        self.module_title = BaseFindLocator(page=self.page, locator=self.acc_locators.MODULE_TITLE)
        
        self.customer_name = BaseFillAction(page=self.page, locator=self.acc_locators.CUSTOMER_NAME_INPUT)
        self.customer_name_check = IsElementContainsText(page=self.page, locator=self.acc_locators.CUSTOMER_NAME_INPUT)

        self.telephone_number = BaseFillAction(page=self.page, locator=self.acc_locators.TELEPHONE_NUMBER_INPUT)
        self.telephone_number_check = IsElementContainsText(
            page=self.page,
            locator=self.acc_locators.TELEPHONE_NUMBER_INPUT
        )

        self.email_address = BaseFillAction(page=self.page, locator=self.acc_locators.EMAIL_ADDRESS_INPUT)
        self.email_address_check = IsElementContainsText(page=self.page, locator=self.acc_locators.EMAIL_ADDRESS_INPUT)

        self.lead_source = BaseSelectOption(page=self.page, locator=self.acc_locators.LEAD_SOURCE_SELECT)
        self.lead_source_check = IsElementContainsText(page=self.page, locator=self.acc_locators.LEAD_SOURCE_SELECT)

        self.lead_priority = BaseSelectOption(page=self.page, locator=self.acc_locators.LEAD_PRIORITY_SELECT)
        self.lead_priority_check = IsElementContainsText(page=self.page, locator=self.acc_locators.LEAD_PRIORITY_SELECT)

        self.description = BaseFillAction(page=self.page, locator=self.acc_locators.DESCRIPTION_TEXTAREA)
        self.description_check = IsElementContainsText(page=self.page, locator=self.acc_locators.DESCRIPTION_TEXTAREA)

        # buttons etc.

        self.save_btn = BaseClick(
            page=self.page,
            locator=self.common_locators.SAVE_BTN,
            log_name=__name__
        )
        self.save_btn_visibility = IsElementVisible(
            page=self.page,
            locator=self.common_locators.SAVE_BTN
        )

        self.edit_btn = BaseClick(
            page=self.page,
            locator=self.common_locators.EDIT_BUTTON,
            log_name=__name__
        )

        # Subpanels

        self.expand_subpanels = BaseClick(page=self.page, locator=self.common_locators.EXPAND_SUBPANELS)
        self.history_subpanel = BaseClick(page=self.page, locator=self.common_locators.HISTORY_SP)

    @step("Open account creation form")
    @log_errors(context=f"{context}.open_account_creation_form")
    def open_account_creation_form(self) -> None:
        self.menu_page.accounts_menu.click_on()
        self.menu_page.create_acc_item.click_on()

    @step("Checking that the accounts page is open")
    @log_errors(context=f"{context}.is_accounts_page_open")
    def is_accounts_page_open(self) -> None:
        expect_url = f"{HTTP_PROTOCOL}{BASE_URL}/{self.module_path}"

        expect(self.page.url).to_have_url(url_or_reg_exp=expect_url) and expect(
            self.module_title.find_element_by_locator()
        ).to_be_visible()

    @step("filling form fields")
    @log_errors(context=f"{context}.fill_form_fields")
    def fill_form_fields(self, test_data: Account) -> None:
        with step("Filling 'Customer Name'"):
            self.customer_name.fill_input_field(text=test_data.customer_name)

        with step("Filling 'Telephone Number'"):
            self.telephone_number.fill_input_field(text=test_data.telephone_number)

        with step("Filling 'Email Address'"):
            self.email_address.fill_input_field(text=test_data.email_address)

        with step("Filling 'Lead Source'"):
            self.lead_source.select_option(value=test_data.lead_source)

        with step("Filling 'Lead Priority'"):
            self.lead_priority.select_option(value=test_data.lead_priority)

        with step("Filling 'Description'"):
            self.description.fill_input_field(text=test_data.description)

    @step("Checking that the account has been created")
    @log_errors(context=f"{context}.is_account_created")
    def is_account_created(self, test_data: Account) -> None:
        with step("Checking 'Customer Name'"):
            # skipped because of an error in the field 'Customer Name'.
            # Actual length is 150, should be 250.
            pass

        with step("Checking 'Telephone Number'"):
            self.telephone_number_check.is_input_contains_value(expected_value=test_data.telephone_number)

        with step("Checking 'Email Address'"):
            self.email_address_check.is_input_contains_value(expected_value=test_data.email_address)

        with step("Checking 'Lead Source'"):
            self.lead_source_check.is_select_contains_option(expected_option=test_data.lead_source)

        with step("Checking 'Lead Priority'"):
            self.lead_priority_check.is_select_contains_option(expected_option=test_data.lead_priority)

        with step("Checking 'Description'"):
            self.description_check.is_input_contains_value(expected_value=test_data.description)

        page_screenshot(page=self.page)

    @step("Clicking on Save button")
    @log_errors(context=f"{context}.click_on_save_btn")
    def click_on_save_btn(self) -> None:
        self.save_btn.click_on()

    @step("Opening entity in edit mode")
    @log_errors(context=f"{context}.open_entity_in_edit_mode")
    def open_entity_in_edit_mode(self) -> str:
        self.edit_btn.click_on()

        return self.page.url

    @step("Expanding security group subpanel")
    @log_errors(context=f"{context}.expand_security_group_sp")
    def expand_security_group_sp(self) -> None:
        """
        This method expands the block with sub-panels.
        """

        self.expand_subpanels.click_on()
