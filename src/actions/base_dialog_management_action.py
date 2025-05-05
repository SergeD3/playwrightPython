from playwright.sync_api import Page, expect
from src.actions.base_click_action import BaseClick
from src.checks.common.is_element_visible import IsElementVisible
from src.locators.common_locators import CommonLocators
from src.utils.logging import log_errors


class BaseDialogManagementAction:
    context = "BaseDialogManagementAction"
    common_locators = CommonLocators()

    def __init__(self, page: Page):
        # configuration

        self.page = page

        # buttons

        self.proceed_button = BaseClick(page=self.page, locator=self.common_locators.CONFIRMATION_PROCEED_BUTTON)
        self.proceed_button_check = IsElementVisible(
            page=self.page,
            locator=self.common_locators.CONFIRMATION_PROCEED_BUTTON
        )

        self.cancel_button = BaseClick(page=self.page, locator=self.common_locators.CONFIRMATION_CANCEL_BUTTON)
        self.cancel_button_check = IsElementVisible(
            page=self.page,
            locator=self.common_locators.CONFIRMATION_CANCEL_BUTTON
        )

    @log_errors(context=f"{context}.accept_dialog", message="Accept dialog")
    def accept_dialog(self):
        """BaseDialogManagementAction.accept_dialog

        This method clicking on 'Proceed' button on confirmation dialog.

        """
        expect(self.proceed_button.find_element.find_element_by_locator()).to_be_visible(visible=True)
        self.proceed_button.click_on()

    @log_errors(context=f"{context}.dismiss_dialog", message="Dismiss dialog")
    def dismiss_dialog(self):
        """BaseDialogManagementAction.dismiss_dialog

        This method clicking on 'Cancel' button on confirmation dialog.

        """
        expect(self.cancel_button.find_element.find_element_by_locator()).to_be_visible(visible=True)
        self.cancel_button.click_on()
