
class TasksPageLocators:

    # creation form fields

    PRIORITY_SELECT = "xpath=//*[contains(@class, 'field-name-priority')]/descendant::select"
    STATUS_SELECT = "xpath=//*[contains(@class, 'field-name-status')]/descendant::select"
    PARENT_TYPE_SELECT = "xpath=//*[contains(@class, 'name-parent_type')]/descendant::select"
    RELATED_TO_SUGGEST = "xpath=//*[contains(@class, 'name-parent_name')]/descendant::*[contains(@id, 'pn_id')]"
    CONTACT_SUGGEST = "xpath=//*[contains(@class, 'name-contact_name')]/descendant::*[contains(@id, 'pn_id')]"
