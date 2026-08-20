def classify_capital_allocation(cfo, cfi, cff, pat=None):
    s_cfo = "+" if cfo >= 0 else "-"
    s_cfi = "+" if cfi >= 0 else "-"
    s_cff = "+" if cff >= 0 else "-"
    pattern = f"({s_cfo},{s_cfi},{s_cff})"
    
    mapping = {
        "(+,-,-)": "Reinvestor",
        "(+,+,-)": "Liquidating Assets",
        "(-,+,+)": "Distress Signal",
        "(-,-,+)": "Growth Funded by Debt",
        "(+,+,+)": "Cash Accumulator",
        "(-,-,-)": "Pre-Revenue",
        "(+,-,+)": "Mixed"
    }
    label = mapping.get(pattern, "Mixed")
    if pattern == "(+,-,-)" and pat and pat > 0 and (cfo / pat) > 1.2:
        label = "Shareholder Returns"
    return pattern, label
