def calculate_pph(salary, rules):
    tax = 0
    for rule in rules:
        if salary > rule.min_income:
            taxable = min(salary, rule.max_income) - rule.min_income
            tax += taxable * rule.rate
    return tax