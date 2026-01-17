from pydantic import BaseModel, Field

class TaxRuleCreate(BaseModel):
    min_income: float = Field(..., ge=0)
    max_income: float = Field(..., gt=0)
    rate: float = Field(..., gt=0, le=1)
