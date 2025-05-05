
class CommonLocators:

    # common elements of the creation form
    
    CREATE_TITLE = "xpath=//span[text()='Create']"

    NAME_INPUT = "xpath=//*[contains(@class, 'name-name')]/descendant::input"
    FIRST_NAME = "xpath=//*[contains(@class, 'name-first_name')]/descendant::input"
    LAST_NAME = "xpath=//*[contains(@class, 'name-last_name')]/descendant::input"
    EMAIL = "xpath=//*[contains(@class, 'name-email_address')]/descendant::input"
    DESCRIPTION_TEXTAREA = "xpath=//*[contains(@class, 'name-description')]/descendant::textarea"
    DESCRIPTION_LABEL = "xpath=//label[contains(text(), 'DESCRIPTION')]"
    JOB_TITLE = "xpath=//*[contains(@class, 'name-title')]/descendant::input"
    MOBILE_PHONE = "xpath=//*[contains(@class, 'name-phone_mobile')]/descendant::input"

    # buttons

    SAVE_BTN = "xpath=//*[contains(text(), 'Save')]/parent::button"
    CANCEL_BTN = "xpath=//*[contains(text(), 'Cancel')]/parent::button"
    EDIT_BUTTON = "xpath=//*[contains(text(), 'Edit')]/ancestor::button"
    ACTIONS_BTN = (
        "xpath=//*[@buttonclass='settings-button']/descendant::button[contains(text(),'Actions')]"
    )

    # Actions list items

    DELETE_LINK = "xpath=//div[contains(text(), 'Delete')]/ancestor::a"

    # suggest input field

    ACCOUNT_NAME_SUGGEST = "xpath=//*[contains(@class, 'name-account_name')]/descendant::*[contains(@id, 'pn_id')]/span"
    SUGGEST_INPUT = "xpath=//div[contains(@class, 'p-dropdown-header')]/descendant::input"
    SUGGEST_ITEM = "xpath=//*[contains(@aria-label, '{text}') and @aria-posinset='1']"

    # entity in View mode

    RECORD_NAME_TITLE = "xpath=//*[contains(@class, 'record-view-name')]/descendant::span"

    # subpanel

    EXPAND_SUBPANELS = "xpath=//a[@class='clickable position-relative']"
    SECURITY_GROUP_SP = "xpath=//*[contains(text(), 'Security Groups')]/ancestor::div[@container='body']"
    HISTORY_SP = "xpath=//*[contains(text(),'History')]/ancestor::div[@container='body']"

    # confirmation modal window

    CONFIRMATION_PROCEED_BUTTON = "xpath=//*[contains(text(), 'Proceed')]/parent::button"
    CONFIRMATION_CANCEL_BUTTON = "xpath=//*[contains(text(), 'Cancel')]/parent::button"

    # alert statuses

    ALERT_SUCCESS = "xpath=//div[contains(text(), 'Record deleted successfully')]"
