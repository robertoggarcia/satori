from typing import List

from pydantic import BaseModel


class ApplicationSchema(BaseModel):
    application_id: int
    account_name: str
    uw_name: str
    premium: float
    state: str
    effective_date: str
    expiration_date: str
    sic: str
    status: str
    deal_stage: str
    lines_coverage: List
