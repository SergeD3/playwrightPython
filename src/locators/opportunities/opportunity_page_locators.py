
class OpportunityPageLocators:

    # creation form fields

    CURRENCY_SELECT = "xpath=//*[contains(@class, 'name-currency_id')]/descendant::select"

    # Shadow DOM
    CURRENCY_VALUE_SD = ("div", "USD")

    AMOUNT_INPUT = "xpath=//*[contains(@class, 'name-amount')]/descendant::input"
    SALES_STAGE_SELECT = "xpath=//*[contains(@class, 'sales_stage')]/descendant::select"

    # calendar field

    EXP_CLOSE_DATE_FIELD = "xpath=//div[contains(@class, 'field-datetime-edit')]/input"
    CALENDAR_DATE = "xpath=//*[@role='gridcell' and @tabindex='0']"

    # shadow DOM calendar elements

    OPPORTUNITY_TYPE = "xpath=//*[contains(@class, 'name-opportunity_type')]/descendant::select"
    LEAD_SOURCE = "xpath=//*[contains(@class, 'name-lead_source')]/descendant::select"
    NEXT_STEP = "xpath=//*[contains(@class, 'field-name-next_step')]/descendant::input"
    PROBABILITY = "xpath=//*[contains(@class, 'field-name-probability')]/descendant::input"
