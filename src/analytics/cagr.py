def calculate_cagr(start_val, end_val, periods):
    if periods <= 0:
        return None, "INSUFFICIENT"
    if start_val == 0:
        return None, "ZERO_BASE"
    if start_val > 0 and end_val > 0:
        val = round(((end_val / start_val) ** (1 / periods) - 1) * 100, 2)
        return val, "NORMAL"
    elif start_val > 0 and end_val <= 0:
        return None, "DECLINE_TO_LOSS"
    elif start_val < 0 and end_val > 0:
        return None, "TURNAROUND"
    else:
        return None, "BOTH_NEGATIVE"
