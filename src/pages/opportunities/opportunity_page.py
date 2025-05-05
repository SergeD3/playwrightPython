from allure import step
from playwright.sync_api import Page
from src.checks.common.is_element_contains_text import IsElementContainsText
from src.locators.common_locators import CommonLocators
from src.pages.menu.menu_page import MenuPage
from src.actions.base_find_locator_action import BaseFindLocator
from src.actions.base_fill_action import BaseFillAction
from src.actions.base_click_action import BaseClick
from src.actions.base_select_action import BaseSelectOption
from src.checks.common.is_element_visible import IsElementVisible
from src.locators.opportunities.opportunity_page_locators import OpportunityPageLocators
from src.components.common.suggest_input_component import SuggestInputComponent
from src.components.common.calendar_input_component import CalendarInputComponent
from src.utils.logging import log_errors
from src.actions.take_screenshot_action import page_screenshot


class OpportunityPage:
    opportunities_loc = OpportunityPageLocators()
    common_locators = CommonLocators()
    context = "OpportunityPage"

    def __init__(self, page: Page):
        self.page = page
        self.menu_page = MenuPage(page)

        # creation form fields

        self.opp_name = BaseFillAction(
            page=page, locator=self.common_locators.NAME_INPUT
        )
        self.opp_name_check = IsElementContainsText(
            page=page, locator=self.common_locators.NAME_INPUT
        )

        self.currency_select = BaseSelectOption(
            page=page, locator=self.opportunities_loc.CURRENCY_SELECT
        )

        self.acc_name = SuggestInputComponent(
            page=page, locator=self.common_locators.ACCOUNT_NAME_SUGGEST
        )

        self.opportunity_amount = BaseFillAction(
            page=page, locator=self.opportunities_loc.AMOUNT_INPUT
        )
        self.opportunity_amount_check = IsElementContainsText(
            page=page, locator=self.opportunities_loc.AMOUNT_INPUT
        )

        self.sales_stage = BaseSelectOption(
            page=page, locator=self.opportunities_loc.SALES_STAGE_SELECT
        )

        self.probability = BaseFillAction(
            page=page, locator=self.opportunities_loc.PROBABILITY
        )
        self.probability_check = IsElementContainsText(
            page=page, locator=self.opportunities_loc.PROBABILITY
        )

        self.next_step = BaseFillAction(
            page=page, locator=self.opportunities_loc.NEXT_STEP
        )
        self.next_step_check = IsElementContainsText(
            page=page, locator=self.opportunities_loc.NEXT_STEP
        )

        self.description = BaseFillAction(
            page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA
        )
        self.description_check = IsElementContainsText(
            page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA
        )

        self.exp_close_date = CalendarInputComponent(
            page=page, locator=self.opportunities_loc.EXP_CLOSE_DATE_FIELD
        )
        self.exp_close_date_check = IsElementContainsText(
            page=page, locator=self.opportunities_loc.EXP_CLOSE_DATE_FIELD
        )

        self.opp_type = BaseSelectOption(
            page=page, locator=self.opportunities_loc.OPPORTUNITY_TYPE
        )
        self.lead_source = BaseSelectOption(
            page=page, locator=self.opportunities_loc.LEAD_SOURCE
        )

        # buttons, checkboxes etc.

        self.save_btn = BaseClick(
            page=page, locator=self.common_locators.SAVE_BTN, log_name=__name__
        )
        self.save_btn_visibility = IsElementVisible(
            page=page, locator=self.common_locators.SAVE_BTN
        )

        self.edit_btn = BaseClick(
            page=page, locator=self.common_locators.EDIT_BUTTON, log_name=__name__
        )

        # checks

        self.find_record_title = BaseFindLocator(
            page=page, locator=self.common_locators.RECORD_NAME_TITLE
        )

        # Subpanels

        self.security_group = BaseClick(page=self.page, locator=self.common_locators.SECURITY_GROUP_SP)

    @step("Open creation form")
    @log_errors(context=f"{context}.open_creation_form")
    def open_creation_form(self) -> None:
        self.menu_page.opportunity_menu.click_on_menu_item()
        self.menu_page.create_opportunity_item.click_on_menu_item()

    @step("Filling form fields")
    @log_errors(context=f"{context}.fill_form_fields")
    def fill_form_fields(self, test_data: dict) -> None:
        with step("Filling 'Opportunity Name'"):
            self.opp_name.fill_input_field(text=test_data.get("opportunity_name"))

        with step("Filling 'Currency Value'"):
            self.currency_select.select_option(value=test_data.get("currency_value"))

        with step("Filling 'Sales Stage'"):
            self.sales_stage.select_option(value=test_data.get("sales_stage"))

        with step("Filling 'Probability'"):
            self.probability.fill_input_field(text=test_data.get("probability"))

        with step("Filling 'Next Step'"):
            self.next_step.fill_input_field(text=test_data.get("next_step"))

        with step("Filling 'Opportunity Amount'"):
            self.opportunity_amount.fill_input_field(text=test_data.get("opportunity_amount"))

        with step("Filling 'Description'"):
            self.description.fill_input_field(text=test_data.get("description"))

        with step("Filling 'Account Name'"):
            self.acc_name.set_value_and_select(value=test_data.get("account_name"))

        with step("Filling 'EXPECTED CLOSE DATE'"):
            self.exp_close_date.set_current_date()

        with step("Filling 'Opportunity Type'"):
            self.opp_type.select_option(value=test_data.get("opportunity_type"))

        with step("Filling 'Lead Source'"):
            self.lead_source.select_option(value=test_data.get("lead_source"))

    @step("Click on 'Save' button")
    @log_errors(context=f"{context}.click_on_save_button")
    def click_on_save_button(self) -> None:
        self.save_btn.click_on()

    @step("Checking that the record has been created")
    @log_errors(context=f"{context}.is_record_created")
    def is_record_created(self, test_data: dict) -> None:
        with step("Checking 'Opportunity Name'"):
            self.opp_name_check.is_input_contains_value(
                expected_value=test_data.get("opportunity_name")
            )

        with step("Checking 'Probability'"):
            self.probability_check.is_input_contains_value(
                expected_value=test_data.get("probability")
            )

        with step("Checking 'Next Step'"):
            self.next_step_check.is_input_contains_value(
                expected_value=test_data.get("next_step")
            )

        with step("Checking 'Description'"):
            self.description_check.is_input_contains_value(
                expected_value=test_data.get("description")
            )

        with step("Checking 'Current Day'"):
            self.exp_close_date_check.is_input_contains_value(
                expected_value=test_data.get("current_day")["full-date"]
            )

        page_screenshot(page=self.page)

    @step("Opening entity in edit mode")
    @log_errors(context=f"{context}.open_entity_in_edit_mode")
    def open_entity_in_edit_mode(self) -> None:
        self.expand_security_group_sp()
        self.edit_btn.click_on()

    @step("Expanding security group subpanel")
    @log_errors(context=f"{context}.expand_security_group_sp")
    def expand_security_group_sp(self):
        self.security_group.click_on()
