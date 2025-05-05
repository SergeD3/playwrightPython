from allure import step
from playwright.sync_api import Page
from src.locators.common_locators import CommonLocators
from src.locators.tasks.tasks_page_locators import TasksPageLocators
from src.pages.base_page import BasePage
from src.pages.menu.menu_page import MenuPage
from src.actions.base_fill_action import BaseFillAction
from src.actions.base_select_action import BaseSelectOption
from src.checks.common.is_element_contains_text import IsElementContainsText
from src.components.common.suggest_input_component import SuggestInputComponent
from src.checks.common.is_element_visible import IsElementVisible
from src.actions.base_click_action import BaseClick
from src.actions.take_screenshot_action import page_screenshot
from src.utils.env import BASE_URL
from src.utils.logging import log_errors


class TaskPage(BasePage):
    common_locators = CommonLocators()
    task_locators = TasksPageLocators()
    context = "TaskPage"
    
    tasks_path = "#/tasks"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.menu_page = MenuPage(page)
        
        # creation form fields
        
        self.fill_subject_field = BaseFillAction(page=self.page, locator=self.common_locators.NAME_INPUT)
        self.subject_check = IsElementContainsText(
            page=page, locator=self.common_locators.NAME_INPUT
        )
        
        self.priority_select = BaseSelectOption(page=self.page, locator=self.task_locators.PRIORITY_SELECT)
        self.priority_check = IsElementContainsText(page=page, locator=self.task_locators.PRIORITY_SELECT)
        
        self.description = BaseFillAction(
            page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA
        )
        self.description_check = IsElementContainsText(
            page=page, locator=self.common_locators.DESCRIPTION_TEXTAREA
        )
        
        self.status_select = BaseSelectOption(page=self.page, locator=self.task_locators.STATUS_SELECT)
        self.status_check = IsElementContainsText(page=self.page, locator=self.task_locators.STATUS_SELECT)
        
        self.parent_type_select = BaseSelectOption(page=self.page, locator=self.task_locators.PARENT_TYPE_SELECT)
        self.related_to_suggest = SuggestInputComponent(page=self.page, locator=self.task_locators.RELATED_TO_SUGGEST)
        self.contact_suggest = SuggestInputComponent(page=self.page, locator=self.task_locators.CONTACT_SUGGEST)

        # buttons etc.
        
        self.save_btn = BaseClick(
            page=page, locator=self.common_locators.SAVE_BTN, log_name=__name__
        )
        self.save_btn_visibility = IsElementVisible(
            page=page, locator=self.common_locators.SAVE_BTN
        )
        
        self.edit_btn = BaseClick(
            page=page, locator=self.common_locators.EDIT_BUTTON, log_name=__name__
        )

        # Subpanels

        self.security_group = BaseClick(page=self.page, locator=self.common_locators.SECURITY_GROUP_SP)

    @step("Open creation form")
    @log_errors(context=f"{context}.open_creation_form")
    def open_creation_form(self) -> None:
        # 'More' menu
        
        self.open_tasks_page_via_more_menu()
        
        # 'Tasks' menu
        
        self.menu_page.tasks_menu.click_on_menu_item()
        self.menu_page.create_tasks_item.click_on_menu_item()

    @step("Opening tasks page via more menu")
    @log_errors(context=f"{context}.open_tasks_page_via_more_menu")
    def open_tasks_page_via_more_menu(self):
        self.menu_page.more_menu.click_on_menu_item()
        self.menu_page.tasks_in_more_menu.click_on_menu_item()
        self.page.wait_for_url(url=f"{BASE_URL}/{self.tasks_path}")

    @step("Filling form fields")
    @log_errors(context=f"{context}.fill_form_fields")
    def fill_form_fields(self, test_data: dict) -> None:
        with step("Filling 'Subject'"):
            self.fill_subject_field.fill_input_field(text=test_data.get("subject"))

        with step("Filling 'Priority'"):
            self.priority_select.select_option(value=test_data.get("priority"))

        with step("Filling 'Description'"):
            self.description.fill_input_field(text=test_data.get("description"))

        with step("Filling 'Status'"):
            self.status_select.select_option(value=test_data.get("status"))

        with step("Filling 'Parent Type'"):
            self.parent_type_select.select_option(value=test_data.get("parent_type"))

        with step("Filling 'Related To'"):
            self.related_to_suggest.set_value_and_select(value=test_data.get("related_to"))

        with step("Filling 'Contact'"):
            self.contact_suggest.set_value_and_select(value=test_data.get("contact"))

    @step("Click on 'Save' button")
    @log_errors(context=f"{context}.click_on_save_button")
    def click_on_save_button(self) -> None:
        self.save_btn.click_on()

    @step("Checking that the record has been created")
    @log_errors(context=f"{context}.is_record_created")
    def is_record_created(self, test_data: dict) -> None:
        with step("Checking 'Subject'"):
            self.subject_check.is_input_contains_value(expected_value=test_data.get("subject"))

        with step("Checking 'Priority'"):
            self.priority_check.is_select_contains_option(expected_option=test_data.get("priority"))

        with step("Checking 'Description'"):
            self.description_check.is_input_contains_value(expected_value=test_data.get("description"))

        with step("Checking 'Status'"):
            self.status_check.is_select_contains_option(expected_option=test_data.get("status"))

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
