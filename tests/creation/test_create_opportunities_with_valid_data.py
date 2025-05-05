from allure import title, feature, step
from pytest import mark
from src.helpers import common_helper as cmh
from src.pages.opportunities.opportunity_page import OpportunityPage


class TestCreateOpportunitiesWithValidData:

    @feature("Creation")
    @title("Test create opportunities with valid data")
    @mark.smoke
    @mark.parametrize("test_data", [
        {
            "opportunity_name": cmh.get_random_string(length=3),
            "currency_value": None,
            "account_name": None,
            "opportunity_amount": str(cmh.get_random_number(length=4)),
            "probability": str(cmh.get_random_number(length=2)),
            "next_step": cmh.get_random_string(length=3),
            "sales_stage": None,
            "description": cmh.get_random_string(length=256),
            "current_day": cmh.get_current_date(),
            "opportunity_type": None,
            "lead_source": None
        },
        {
            "opportunity_name": cmh.get_random_string(length=50),
            "currency_value": None,
            "account_name": None,
            "opportunity_amount": str(cmh.get_random_number(length=8)),
            "probability": str(cmh.get_random_number(length=2)),
            "next_step": cmh.get_random_string(length=100),
            "sales_stage": None,
            "description": cmh.get_random_string(length=520),
            "current_day": cmh.get_current_date(),
            "opportunity_type": None,
            "lead_source": None
        }
    ])
    def test_create_opportunities_with_valid_data(self, authenticated_session, test_data: dict):
        opportunities_page = OpportunityPage(authenticated_session)

        with step("Opening creation form"):
            opportunities_page.open_creation_form()

        with step("Filling form fields"):
            opportunities_page.fill_form_fields(test_data=test_data)

        with step("Clicking on 'Save' button"):
            opportunities_page.click_on_save_button()

        with step("Opening entity in edit mode"):
            opportunities_page.open_entity_in_edit_mode()

        with step("Checking that the entity has been created"):
            opportunities_page.is_record_created(test_data=test_data)
