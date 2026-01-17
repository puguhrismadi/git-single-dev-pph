from sqlalchemy.orm import Session
from app.models import TaxRule

def create_tax_rule(
    db: Session,
    min_income: float,
    max_income: float,
    rate: float
):
    rule = TaxRule(
        min_income=min_income,
        max_income=max_income,
        rate=rate
    )
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule
