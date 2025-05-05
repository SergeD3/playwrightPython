from allure import step
from src.utils.logging import log_errors
from src.checks.common.is_element_visible import IsElementVisible
from src.locators.common_locators import CommonLocators
from src.pages.menu.menu_page import MenuPage
from src.actions.base_fill_action import BaseFillAction
from src.actions.base_click_action import BaseClick
from src.components.common.suggest_input_component import SuggestInputComponent
from src.actions.take_screenshot_action import page_screenshot
from src.checks.common.is_element_contains_text import IsElementContainsText


class ContactsPage:
    context = "ContactsPage"
    common_locators = CommonLocators()

    def __init__(self, page):
        self.page = page
        self.menu_page = MenuPage(page)

        # creation form fields

        self.first_name = BaseFillAction(page=page, locator=self.common_locators.FIRST_NAME)
        self.first_name_check = IsElementContainsText(page=page, locator=self.common_locators.FIRST_NAME)
        
        self.last_name = BaseFillAction(page=page, locator=self.common_locators.LAST_NAME)
        self.last_name_check = IsElementContainsText(page=page, locator=self.common_locators.LAST_NAME)
        
        self.job_title = BaseFillAction(page=page, locator=self.common_locators.JOB_TITLE)
        self.job_title_check = IsElementContainsText(page=page, locator=self.common_locators.JOB_TITLE)
        
        self.account_name = SuggestInputComponent(page=page, locator=self.common_locators.ACCOUNT_NAME_SUGGEST)
        
        self.email = BaseFillAction(page=page, locator=self.common_locators.EMAIL)
        self.email_check = IsElementContainsText(page=page, locator=self.common_locators.EMAIL)
        
        self.description = BaseFillAction(page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA)
        self.description_check = IsElementContainsText(page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA)
        
        self.mobile_phone = BaseFillAction(page=page, locator=self.common_locators.MOBILE_PHONE)
        self.mobile_phone_check = IsElementContainsText(page=page, locator=self.common_locators.MOBILE_PHONE)

        # buttons etc.

        self.save_btn = BaseClick(
            page=self.page, locator=self.common_locators.SAVE_BTN, log_name=__name__
        )
        self.save_btn_visibility = IsElementVisible(
            page=self.page, locator=self.common_locators.SAVE_BTN
        )

        self.edit_btn = BaseClick(
            page=self.page, locator=self.common_locators.EDIT_BUTTON, log_name=__name__
        )

        # Subpanels

        self.security_group = BaseClick(page=self.page, locator=self.common_locators.SECURITY_GROUP_SP)

    @step("Open contact creation form")
    @log_errors(context=f"{context}.open_contact_creation_form")
    def open_contact_creation_form(self):
        self.menu_page.contacts_menu.click_on_menu_item()
        self.menu_page.create_contact_item.click_on_menu_item()

    @step("Filling form fields")
    @log_errors(context=f"{context}.fill_form_fields")
    def fill_form_fields(self, test_data: dict) -> None:
        with step("Filling 'First Name'"):
            self.first_name.fill_input_field(text=test_data.get('first_name'))
        
        with step("Filling 'Last Name'"):
            self.last_name.fill_input_field(text=test_data.get('last_name'))
        
        with step("Filling 'Job Title'"):
            self.job_title.fill_input_field(text=test_data.get('job_title'))
        
        with step("Filling 'Account Name'"):
            self.account_name.set_value_and_select(value=test_data.get("account_name"))
        
        with step("Filling 'Email'"):
            self.email.fill_input_field(text=test_data.get('email'))
        
        with step("Filling 'Description'"):
            self.description.fill_input_field(text=test_data.get('description'))
        
        with step("Filling 'Mobile Phone'"):
            self.mobile_phone.fill_input_field(text=test_data.get('mobile_phone'))

    @step("Click on 'Save' button")
    @log_errors(context=f"{context}.click_on_save_button")
    def click_on_save_button(self):
        self.save_btn.click_on()

    @step("Checking that the contact has been created")
    @log_errors(context=f"{context}.is_contact_created")
    def is_contact_created(self, test_data: dict) -> None:
        with step("Checking 'First Name'"):
            self.first_name_check.is_input_contains_value(expected_value=test_data.get('first_name'))
        
        with step("Checking 'Last Name'"):
            self.last_name_check.is_input_contains_value(expected_value=test_data.get('last_name'))
        
        with step("Checking 'Job Title'"):
            self.job_title_check.is_input_contains_value(expected_value=test_data.get('job_title'))

        with step("Checking 'Email'"):
            self.email_check.is_input_contains_value(expected_value=test_data.get('email'))

        with step("Checking 'Description'"):
            self.description_check.is_input_contains_value(expected_value=test_data.get('description'))

        with step("Checking 'Mobile Phone'"):
            self.mobile_phone_check.is_input_contains_value(expected_value=test_data.get('mobile_phone'))
        
        page_screenshot(self.page)

    @step("Opening entity in edit mode")
    @log_errors(context=f"{context}.open_entity_in_edit_mode")
    def open_entity_in_edit_mode(self) -> None:
        self.expand_security_group_sp()
        self.edit_btn.click_on()

    @step("Expanding security group subpanel")
    @log_errors(context=f"{context}.expand_security_group_sp")
    def expand_security_group_sp(self):
        self.security_group.click_on()
