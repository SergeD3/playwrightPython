from pydantic import BaseModel


class Account(BaseModel):

    # 'OVERVIEW' tab

    customer_name: str
    tin: int
    prime: str = ""
    legal_status: str
    residency: bool = True
    brand_name: str
    scope_activity: str
    number_employees: str = ""
    legal_status_company: str = ""
    telephone_number: str = ""
    email_address: str = ""
    lead_source: str = ""
    restricted: bool = False
    lead_priority: str = ""

    # 'MANUALLY ENTERED' tab

    non_customer: bool = False
    description: str = ""
    annual_turnover: str = None
    engagement_notes: str = ""
    customer_satisfaction_score: str = ""
    preferred_service_channels: str = ""
    marketing_opt_ins: str = ""
    referral_source: str = ""
    engagement_level: str = ""
    campaign_history: str = ""
