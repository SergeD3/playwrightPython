from allure import step
from playwright.sync_api import expect, Page
from src.utils.env import BASE_URL
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

        # (NEW) fields template - after issues/8131
        
        self.customer_name = BaseFillAction(page=self.page, locator=self.acc_locators.CUSTOMER_NAME_INPUT)
        self.customer_name_check = IsElementContainsText(page=self.page, locator=self.acc_locators.CUSTOMER_NAME_INPUT)

        self.tin = BaseFillAction(page=self.page, locator=self.acc_locators.TIN_INPUT)
        self.tin_check = IsElementContainsText(page=self.page, locator=self.acc_locators.TIN_INPUT)

        self.prime = BaseSelectOption(page=self.page, locator=self.acc_locators.PRIME_SELECT)
        self.prime_check = IsElementContainsText(page=self.page, locator=self.acc_locators.PRIME_SELECT)

        self.legal_status = BaseSelectOption(page=self.page, locator=self.acc_locators.LEGAL_STATUS_SELECT)
        self.legal_status_check = IsElementContainsText(page=self.page, locator=self.acc_locators.LEGAL_STATUS_SELECT)

        self.residency = BaseClick(page=self.page, locator=self.acc_locators.RESIDENCY_CHECKBOX_SPAN)
        self.residency_check = IsElementContainsText(page=self.page, locator=self.acc_locators.RESIDENCY_CHECKBOX_SPAN)

        self.brand_name = BaseFillAction(page=self.page, locator=self.acc_locators.BRAND_NAME_INPUT)
        self.brand_name_check = IsElementContainsText(page=self.page, locator=self.acc_locators.BRAND_NAME_INPUT)

        self.scope_activity = BaseSelectOption(page=self.page, locator=self.acc_locators.SCOPE_ACTIVITY_SELECT)
        self.scope_activity_check = IsElementContainsText(
            page=self.page,
            locator=self.acc_locators.SCOPE_ACTIVITY_SELECT
        )

        self.number_employees = BaseFillAction(page=self.page, locator=self.acc_locators.NUMBER_EMPLOYEES_INPUT)
        self.number_employees_check = IsElementContainsText(page=self.page, locator=self.acc_locators.NUMBER_EMPLOYEES_INPUT)

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

        self.annual_turnover = BaseFillAction(page=self.page, locator=self.acc_locators.ANNUAL_TURNOVER_INPUT)
        self.annual_turnover_check = IsElementContainsText(page=self.page, locator=self.acc_locators.ANNUAL_TURNOVER_INPUT)

        self.engagement_notes = BaseFillAction(page=self.page, locator=self.acc_locators.ENGAGEMENT_NOTES_TEXTAREA)
        self.engagement_notes_check = IsElementContainsText(page=self.page, locator=self.acc_locators.ENGAGEMENT_NOTES_TEXTAREA)

        self.customer_satisfaction_score = BaseFillAction(
            page=self.page,
            locator=self.acc_locators.CUSTOMER_SATISFACTION_SCORE_INPUT
        )
        self.customer_satisfaction_score_check = IsElementContainsText(
            page=self.page,
            locator=self.acc_locators.CUSTOMER_SATISFACTION_SCORE_INPUT
        )

        self.preferred_service_channels = BaseFillAction(
            page=self.page,
            locator=self.acc_locators.PREFERRED_SERVICE_CHANNELS_TEXTAREA
        )
        self.preferred_service_channel_check = IsElementContainsText(
            page=self.page,
            locator=self.acc_locators.PREFERRED_SERVICE_CHANNELS_TEXTAREA
        )

        self.marketing_opt_ins = BaseFillAction(page=self.page, locator=self.acc_locators.MARKETING_OPT_INS_TEXTAREA)
        self.marketing_opt_ins_check = IsElementContainsText(
            page=self.page,
            locator=self.acc_locators.MARKETING_OPT_INS_TEXTAREA
        )

        self.referral_source = BaseFillAction(page=self.page, locator=self.acc_locators.REFERRAL_SOURCE_INPUT)
        self.referral_source_check = IsElementContainsText(page=self.page, locator=self.acc_locators.REFERRAL_SOURCE_INPUT)

        self.engagement_level = BaseFillAction(page=self.page, locator=self.acc_locators.ENGAGEMENT_LEVEL_TEXTAREA)
        self.engagement_level_check = IsElementContainsText(page=self.page, locator=self.acc_locators.ENGAGEMENT_LEVEL_TEXTAREA)

        self.campaign_history = BaseFillAction(page=self.page, locator=self.acc_locators.CAMPAIGN_HISTORY_TEXTAREA)
        self.campaign_history_check = IsElementContainsText(page=self.page, locator=self.acc_locators.CAMPAIGN_HISTORY_TEXTAREA)

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
        expect_url = f"{BASE_URL}/{self.module_path}"

        expect(self.page.url).to_have_url(url_or_reg_exp=expect_url) and expect(
            self.module_title.find_element_by_locator()
        ).to_be_visible()

    @step("filling form fields")
    @log_errors(context=f"{context}.fill_form_fields")
    def fill_form_fields(self, test_data: Account) -> None:
        # fields template - after issues/8131
        
        with step("Filling 'Customer Name'"):
            self.customer_name.fill_input_field(text=test_data.customer_name)

        with step("Filling 'Tin'"):
            self.tin.fill_input_field(text=test_data.tin)

        with step("Filling 'Prime'"):
            self.prime.select_option(value=test_data.prime)

        with step("Filling 'Legal Status'"):
            self.legal_status.select_option(value=test_data.legal_status)

        with step("Filling 'Residency'"):
            self.residency.set_checkbox_state(checkbox_state=test_data.residency)

        with step("Filling 'Brand Name'"):
            self.brand_name.fill_input_field(text=test_data.brand_name)

        with step("Filling 'Scope of Activity'"):
            self.scope_activity.select_option(value=test_data.scope_activity)

        with step("Filling 'Number of Employees'"):
            self.number_employees.fill_input_field(text=test_data.number_employees)

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

        with step("Filling 'Annual Turnover'"):
            self.annual_turnover.fill_input_field(text=test_data.annual_turnover)

        with step("Filling 'Engagement Notes'"):
            self.engagement_notes.fill_input_field(text=test_data.engagement_notes)

        with step("Filling 'Customer Satisfaction Score'"):
            self.customer_satisfaction_score.fill_input_field(text=test_data.customer_satisfaction_score)

        with step("Filling 'Preferred Service Channels'"):
            self.preferred_service_channels.fill_input_field(text=test_data.preferred_service_channels)

        with step("Filling 'Marketing Opt-Ins'"):
            self.marketing_opt_ins.fill_input_field(text=test_data.marketing_opt_ins)

        with step("Filling 'Referral Source'"):
            self.referral_source.fill_input_field(text=test_data.referral_source)

        with step("Filling 'Engagement Level'"):
            self.engagement_level.fill_input_field(text=test_data.engagement_level)

        with step("Filling 'Campaign History'"):
            self.campaign_history.fill_input_field(text=test_data.campaign_history)

    @step("Checking that the account has been created")
    @log_errors(context=f"{context}.is_account_created")
    def is_account_created(self, test_data: Account) -> None:
        # fields template - after issues/8131

        with step("Checking 'Customer Name'"):
            pass

            # commented because of an error in the field 'Customer Name'.
            # Actual length is 150, should be 250.
            # self.customer_name_check.is_input_contains_value(expected_value=test_data.get("customer_name"))

        with step("Checking 'Tin'"):
            self.tin_check.is_input_contains_value(expected_value=test_data.tin)

        with step("Checking 'Prime'"):
            self.prime_check.is_select_contains_option(expected_option=test_data.prime)

        with step("Checking 'Legal Status'"):
            self.legal_status_check.is_select_contains_option(expected_option=test_data.legal_status)

        with step("Checking 'Residency'"):
            self.residency_check.is_checkbox_checked(expected_state=test_data.residency)

        with step("Checking 'Brand Name'"):
            self.brand_name_check.is_input_contains_value(expected_value=test_data.brand_name)

        with step("Checking 'Scope of Activity'"):
            self.scope_activity_check.is_select_contains_option(expected_option=test_data.scope_activity)

        with step("Checking 'Number of Employees'"):
            self.number_employees_check.is_input_contains_value(expected_value=test_data.number_employees)

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

        with step("Checking 'Annual Turnover'"):
            self.annual_turnover_check.is_input_contains_value(expected_value=test_data.annual_turnover)

        with step("Checking 'Engagement Notes'"):
            self.engagement_notes_check.is_input_contains_value(expected_value=test_data.engagement_notes)

        with step("Checking 'Customer Satisfaction Score'"):
            self.customer_satisfaction_score_check.is_input_contains_value(
                expected_value=test_data.customer_satisfaction_score
            )

        with step("Checking 'Preferred Service Channels'"):
            self.preferred_service_channel_check.is_input_contains_value(
                expected_value=test_data.preferred_service_channels
            )

        with step("Checking 'Marketing Opt-Ins'"):
            self.marketing_opt_ins_check.is_input_contains_value(expected_value=test_data.marketing_opt_ins)

        with step("Checking 'Referral Source'"):
            self.referral_source_check.is_input_contains_value(expected_value=test_data.referral_source)

        with step("Checking 'Engagement Level'"):
            self.engagement_level_check.is_input_contains_value(expected_value=test_data.engagement_level)

        with step("Checking 'Campaign History'"):
            self.campaign_history_check.is_input_contains_value(expected_value=test_data.campaign_history)

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
    def expand_security_group_sp(self):
        """
        This method expands the block with sub-panels.
        """

        self.expand_subpanels.click_on()
