from allure import title, feature, step
from pytest import mark
from src.helpers import common_helper as cmh
from src.pages.leads.leads_page import LeadsPage


class TestCreateLeadWithValidData:

    @feature("Creation")
    @title("Test create lead with valid data")
    @mark.smoke
    @mark.parametrize("test_data", [
        {
            "first_name": cmh.get_random_name(),
            "last_name": cmh.get_random_last_name(),
            "job_title": cmh.get_random_name(),
            "account_name": f"{cmh.get_random_name()} - {cmh.get_random_last_name()}",
            "email": cmh.get_random_email(),
            "mobile_phone": cmh.get_phone_number()
        }
    ])
    def test_create_lead_with_valid_data(self, authenticated_session, test_data):
        leads_page = LeadsPage(authenticated_session)

        with step("Opening creation form"):
            leads_page.open_lead_creation_form()

        with step("Filling the form fields with valid data"):
            leads_page.fill_form_fields(test_data=test_data)

        with step("Clicking on 'Save' button"):
            leads_page.click_on_save_button()
            
        with step("Opening entity in edit mode"):
            leads_page.open_entity_in_edit_mode()

        with step("Checking that the entity has been created"):
            leads_page.is_lead_created(test_data=test_data)
