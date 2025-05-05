from allure import title, feature, step
from pytest import mark
from src.helpers import common_helper as ch
from src.pages.contacts.contacts_page import ContactsPage


class TestCreateContactWithValidData:

    @feature("Creation")
    @title("Test create contact with valid data")
    @mark.smoke
    @mark.parametrize("test_data", [
        {
            "first_name": ch.get_random_name(),
            "last_name": ch.get_random_last_name(),
            "job_title": ch.get_random_name(),
            "account_name": None,
            "email": ch.get_random_email(),
            "mobile_phone": ch.get_phone_number(),
            "description": ch.get_random_string(length=255),
        }
    ])
    def test_create_contact_with_valid_data(self, authenticated_session, test_data):
        contacts_page = ContactsPage(authenticated_session)

        with step("Opening creation form"):
            contacts_page.open_contact_creation_form()

        with step("Filling the form fields with valid data"):
            contacts_page.fill_form_fields(test_data=test_data)

        with step("Clicking on 'Save' button"):
            contacts_page.click_on_save_button()
            
        with step("Opening entity in edit mode"):
            contacts_page.open_entity_in_edit_mode()

        with step("Checking that the entity has been created"):
            contacts_page.is_contact_created(test_data=test_data)
