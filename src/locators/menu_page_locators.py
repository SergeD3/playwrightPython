
class MenuPageLocators:

    # More menu

    MORE_MENU = "xpath=//*[@labelkey='LBL_MORE']/descendant::li"

    # Accounts menu and its items

    ACCOUNTS_MENU = "xpath=//span[text()='Accounts']/ancestor::a[contains(@class, 'dropdown-toggle')]"
    CREATE_ACCOUNT_ITEM = "xpath=//*[text()='Create Account']/ancestor::a"

    # Contacts menu and its items

    CONTACTS_MENU = "xpath=//span[text()='Contacts']/ancestor::a[contains(@class, 'dropdown-toggle')]"
    CREATE_CONTACTS_ITEM = "xpath=//*[text()='Create Contact']/ancestor::a"

    # Users menu and its items

    USER_ICON_MENU = "xpath=//*[@image='user']/ancestor::ul"
    LOGOUT_MENU_ITEM = "xpath=//a[text()='Logout']/ancestor::scrm-logout-ui"

    # Leads menu and its items

    LEADS_MENU = "xpath=//*[text()='Leads']/ancestor::a[contains(@class, 'dropdown-toggle')]"
    CREATE_LEADS_ITEM = "xpath=//*[text()='Create Lead']/ancestor::a"

    # opportunities and its items
    OPPORTUNITY_MENU = "xpath=//*[text()='Opportunities']/ancestor::a[contains(@class, 'dropdown-toggle')]"
    CREATE_OPPORTUNITY = "xpath=//*[text()='Create Opportunity']/ancestor::a"

    # tasks and its items
    TASKS_MENU_IN_MORE_MENU = "xpath=//*[@labelkey='LBL_MORE']/descendant::*[@href='#/tasks']"
    TASKS_MENU = "xpath=//*[text()='Tasks']/ancestor::a[contains(@class, 'dropdown-toggle')]"
    CREATE_TASK_ITEM = "xpath=//*[text()='Create Task']/ancestor::a"
