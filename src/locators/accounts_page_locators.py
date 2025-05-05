
class AccountsPageLocators:
    MODULE_TITLE = "xpath=//scrm-module-title[contains(text(), 'ACCOUNTS')]"

    # 'OVERVIEW' tab
    # new EV form fields: issues/8131

    CUSTOMER_NAME_INPUT = "xpath=//*[contains(@class, 'field-name-name')]/descendant::input"
    TIN_INPUT = "xpath=//*[contains(@class, 'field-name-tin')]/descendant::input"
    PRIME_SELECT = "xpath=//*[contains(@class, 'field-name-prime')]/descendant::select"
    LEGAL_STATUS_SELECT = "xpath=//*[contains(@class, 'field-name-legal_status')]/descendant::select"
    RESIDENCY_CHECKBOX_SPAN = "xpath=//*[contains(@class, 'field-name-residency')]/descendant::span"
    BRAND_NAME_INPUT = "xpath=//*[contains(@class, 'field-name-brand_name')]/descendant::input"
    SCOPE_ACTIVITY_SELECT = "xpath=//*[contains(@class, 'field-name-activity_scope')]/descendant::select"
    NUMBER_EMPLOYEES_INPUT = "xpath=//*[contains(@class, 'field-name-employees_number')]/descendant::input"
    DISSOLUTION_STATUS_INPUT = "xpath=//*[contains(@class, 'field-name-dissolution_status')]/descendant::input"
    TELEPHONE_NUMBER_INPUT = "xpath=//*[contains(@class, 'field-name-phone_office')]/descendant::input"
    EMAIL_ADDRESS_INPUT = "xpath=//*[contains(@class, 'name-email_address')]/descendant::input[@type='text']"
    LEAD_SOURCE_SELECT = "xpath=//*[contains(@class, 'field-name-lead_source')]/descendant::select"
    LEAD_PRIORITY_SELECT = "xpath=//*[contains(@class, 'field-name-lead_priority')]/descendant::select"
    ASSIGNED_SALES_PERSON_RELATE = (
        "xpath=//*[contains(@class, 'assigned_user_name')]/descendant::span[@role='combobox']"
    )
    RESTRICTED_CHECKBOX_SPAN = "xpath=//*[contains(@class, 'field-name-restricted')]/descendant::span"
    CUSTOMER_STATUS_ENUM = None
    COUNTRY_RESIDENCE_ENUM = None
    LEGAL_STATUS_COMPANY_ENUM = None
    OFFICE_ENUM = None
    DEPARTMENT_ENUM = None

    # 'MANUALLY ENTERED' tab

    NON_CUSTOMER_INPUT = "xpath=//*[contains(@class, 'name-non_customer')]/descendant::input"
    DESCRIPTION_TEXTAREA = "xpath=//*[contains(@class, 'name-description')]/descendant::textarea"
    ANNUAL_TURNOVER_INPUT = "xpath=//*[contains(@class, 'name-annual_turnover')]/descendant::input"
    ENGAGEMENT_NOTES_TEXTAREA = "xpath=//*[contains(@class, 'name-engagement_notes')]/descendant::textarea"
    CUSTOMER_SATISFACTION_SCORE_INPUT = "xpath=//*[contains(@class, 'customer_satisfaction_score')]/descendant::input"
    PREFERRED_SERVICE_CHANNELS_TEXTAREA = (
        "xpath=//*[contains(@class, 'preferred_service_channels')]/descendant::textarea"
    )
    MARKETING_OPT_INS_TEXTAREA = "xpath=//*[contains(@class, 'marketing_opt_ins')]/descendant::textarea"
    REFERRAL_SOURCE_INPUT = "xpath=//*[contains(@class, 'name-referral_source')]/descendant::input"
    ENGAGEMENT_LEVEL_TEXTAREA = "xpath=//*[contains(@class, 'engagement_level')]/descendant::textarea"
    CAMPAIGN_HISTORY_TEXTAREA = "xpath=//*[contains(@class, 'campaign_history')]/descendant::textarea"

    # 'CBS DETAILS' tab

    SOURCE_ORIGIN_INCOMING_FUNDS_ACCOUNT_TEXTAREA = None

    # Account in view mode

    AVERAGE_OPPORTUNITY_TITLE = "xpath=//div[contains(text(), 'OPPORTUNITY PER YEAR')]"

    # Subpanels

    EXPAND_SUBPANELS_LINK = "xpath=//a[@class='clickable position-relative']"
