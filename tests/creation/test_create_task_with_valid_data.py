from allure import feature, title, step
from pytest import mark
from src.pages.tasks.task_page import TaskPage
from src.helpers import common_helper as ch


class TestCreateTaskWithValidData:
    
    @feature("Creation")
    @title("Test create task with valid data")
    @mark.smoke
    @mark.parametrize("test_data", [
        {
            "subject": None,
            "priority": None,
            "description": ch.get_random_string(length=50),
            "status": None,
            "parent_type": None,
            "related_to": None,
            "contact": None
        },
        {
            "subject": f"QA_AUTO {ch.get_random_string(length=15)}",
            "priority": None,
            "description": ch.get_random_string(length=50),
            "status": None,
            "parent_type": None,
            "related_to": None,
            "contact": None
        }
    ])
    def test_create_task_with_valid_data(self, authenticated_session, test_data):
        task_page = TaskPage(authenticated_session)

        with step("Opening creation form"):
            task_page.open_creation_form()

        with step("Filling form fields"):
            task_page.fill_form_fields(test_data=test_data)

        with step("Clicking on 'Save' button"):
            task_page.click_on_save_button()
            
        with step("Opening entity in edit mode"):
            task_page.open_entity_in_edit_mode()

        with step("Checking that the entity has been created"):
            task_page.is_record_created(test_data=test_data)
