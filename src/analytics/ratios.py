def compute_npm(net_profit, sales):
    if not sales or sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)

def compute_roe(net_profit, equity_reserves):
    if not equity_reserves or equity_reserves <= 0:
        return None
    return round((net_profit / equity_reserves) * 100, 2)

def compute_roce(ebit, capital_employed):
    if not capital_employed or capital_employed <= 0:
        return None
    return round((ebit / capital_employed) * 100, 2)

def compute_debt_to_equity(borrowings, equity_reserves):
    if borrowings == 0:
        return 0.0
    if not equity_reserves or equity_reserves <= 0:
        return None
    return round(borrowings / equity_reserves, 2)

def compute_interest_coverage(operating_profit, interest):
    if not interest or interest == 0:
        return None, "Debt Free"
    icr = round(operating_profit / interest, 2)
    label = "Risk" if icr < 1.5 else "Safe"
    return icr, label
