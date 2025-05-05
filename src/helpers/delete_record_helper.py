from allure import step
from playwright.sync_api import Page, expect
from src.actions.base_click_action import BaseClick
from src.locators.common_locators import CommonLocators
from src.utils.logging import log_errors
from src.utils.env import HTTP_PROTOCOL, BASE_URL
from src.actions.base_dialog_management_action import BaseDialogManagementAction
from src.actions.take_screenshot_action import page_screenshot
from src.checks.common.is_element_visible import IsElementVisible


class DeleteRecordHelper:
    common_locators = CommonLocators()
    exception_contexts: list[str] = []
    context: str = "DeleteRecordHelper"

    def __init__(self, page: Page):
        # configuration

        self.page = page

        # buttons

        self.actions_button = BaseClick(page=self.page, locator=self.common_locators.ACTIONS_BTN)
        self.cancel_button = BaseClick(page=self.page, locator=self.common_locators.CANCEL_BTN)

        # other

        self.delete_item_link = BaseClick(page=self.page, locator=self.common_locators.DELETE_LINK)
        self.dialog_actions = BaseDialogManagementAction(page=self.page)
        self.alert_success_check = IsElementVisible(page=self.page, locator=self.common_locators.ALERT_SUCCESS)

    @step("Deleting record")
    @log_errors(context=f"{context}.delete_record", message="Delete record")
    def delete_record(self, url: str, module_path: str):
        with step("Opening detail view"):
            self.page.goto(url=url)
            expect(self.cancel_button.find_element.find_element_by_locator()).not_to_be_visible(timeout=10000)

        with step("Clicking on 'Actions' button"):
            self.actions_button.click_on()

        with step("Clicking on 'Delete' item"):
            self.delete_item_link.click_on()

        with step("Confirm deletion"):
            self.dialog_actions.accept_dialog()

        with step("Checking if the record has been deleted"):
            self.alert_success_check.is_element_visible()

            expect(self.page).to_have_url(
                url_or_reg_exp=f"{HTTP_PROTOCOL}{BASE_URL}/{module_path}",
                timeout=10000
            )

        page_screenshot(page=self.page)
