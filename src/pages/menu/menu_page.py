from src.actions.base_click_action import BaseClick
from src.pages.menu.menu_item import MenuItem
from src.locators.menu_page_locators import MenuPageLocators


class MenuPage:
    menu_loc = MenuPageLocators()

    def __init__(self, page):

        # home menu item

        self.home = MenuItem(page=page, locator=None)

        # accounts menu and its items

        self.accounts_menu = BaseClick(page=page, locator=self.menu_loc.ACCOUNTS_MENU, log_name=__name__)
        self.create_acc_item = BaseClick(page=page, locator=self.menu_loc.CREATE_ACCOUNT_ITEM, log_name=__name__)

        # contacts menu and its items

        self.contacts_menu = MenuItem(page=page, locator=self.menu_loc.CONTACTS_MENU)
        self.create_contact_item = MenuItem(page=page, locator=self.menu_loc.CREATE_CONTACTS_ITEM)

        # users menu and its items

        self.user_icon_menu = MenuItem(page=page, locator=self.menu_loc.USER_ICON_MENU)
        self.logout_menu_item = MenuItem(page=page, locator=self.menu_loc.LOGOUT_MENU_ITEM)

        # leads menu and its items

        self.leads_menu = MenuItem(page=page, locator=self.menu_loc.LEADS_MENU)
        self.create_lead_item = MenuItem(page=page, locator=self.menu_loc.CREATE_LEADS_ITEM)

        # opportunities and its items

        self.opportunity_menu = MenuItem(page=page, locator=self.menu_loc.OPPORTUNITY_MENU)
        self.create_opportunity_item = MenuItem(page=page, locator=self.menu_loc.CREATE_OPPORTUNITY)

        # tasks and its items

        self.tasks_in_more_menu = MenuItem(page=page, locator=self.menu_loc.TASKS_MENU_IN_MORE_MENU)
        self.tasks_menu = MenuItem(page=page, locator=self.menu_loc.TASKS_MENU)
        self.create_tasks_item = MenuItem(page=page, locator=self.menu_loc.CREATE_TASK_ITEM)

        # 'More' menu
        
        self.more_menu = MenuItem(page=page, locator=self.menu_loc.MORE_MENU)
