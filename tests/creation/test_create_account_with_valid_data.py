from allure import title, feature, step
from pytest import mark
from src.pages.accounts.accounts_page import AccountsPage
from src.helpers import common_helper as cmh
from src.pages.accounts.schemas import Account


class TestCreateAccountWithValidData:

    @mark.smoke
    @feature("Creation")
    @title("Test create account with valid data")
    @mark.parametrize("test_data", cmh.get_test_data(module="accounts"))
    def test_create_account_with_valid_data(self, authenticated_session, delete_record, test_data: Account):
        accounts_page = AccountsPage(authenticated_session)

        with step("Opening creation form"):
            accounts_page.open_account_creation_form()

        with step("Filling the form fields with valid data"):
            accounts_page.fill_form_fields(test_data=test_data)

        with step("Clicking on 'Save' button"):
            accounts_page.click_on_save_btn()

        with step("Opening entity in edit mode"):
            entity_url = accounts_page.open_entity_in_edit_mode()

        with step("Checking that the entity has been created"):
            accounts_page.is_account_created(test_data=test_data)

        with step("Deleting entity"):
            delete_record(
                page=authenticated_session,
                url=entity_url,
                module_path=accounts_page.module_path
            )
