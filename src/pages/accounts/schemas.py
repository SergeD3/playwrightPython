from pydantic import BaseModel


class Account(BaseModel):
    customer_name: str
    telephone_number: str = ""
    email_address: str = ""
    lead_source: str = ""
    restricted: bool = False
    lead_priority: str = ""
    description: str = ""
