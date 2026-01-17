from app import models
def calculate_pph(salary, rules):
    tax = 0
    for rule in rules:
        if salary > rule.min_income:
            taxable = min(salary, rule.max_income) - rule.min_income
            tax += taxable * rule.rate
    return tax
def insert_tax_rule(db, min_income, max_income, rate):
    rule = models.TaxRule(min_income=min_income, max_income=max_income, rate=rate)
    db.add(rule)
    db.commit()