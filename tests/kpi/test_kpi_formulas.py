import pytest
from src.analytics.ratios import compute_npm, compute_roe, compute_debt_to_equity, compute_interest_coverage
from src.analytics.cagr import calculate_cagr
from src.analytics.cashflow_kpis import classify_capital_allocation

def test_kpi_suite():
    # Ratios (1-8)
    assert compute_npm(100, 1000) == 10.0
    assert compute_npm(100, 0) is None
    assert compute_roe(150, 1000) == 15.0
    assert compute_roe(150, -500) is None
    assert compute_debt_to_equity(0, 1000) == 0.0
    assert compute_debt_to_equity(500, 1000) == 0.5
    assert compute_interest_coverage(100, 0)[1] == "Debt Free"
    assert compute_interest_coverage(100, 80)[1] == "Risk"

    # CAGR (9-14)
    assert calculate_cagr(100, 200, 3)[1] == "NORMAL"
    assert calculate_cagr(100, -50, 3)[1] == "DECLINE_TO_LOSS"
    assert calculate_cagr(-50, 100, 3)[1] == "TURNAROUND"
    assert calculate_cagr(-50, -100, 3)[1] == "BOTH_NEGATIVE"
    assert calculate_cagr(0, 100, 3)[1] == "ZERO_BASE"
    assert calculate_cagr(100, 200, 0)[1] == "INSUFFICIENT"

    # Cash Flow & Capital Allocation (15-20)
    assert classify_capital_allocation(100, -50, -30)[1] == "Reinvestor"
    assert classify_capital_allocation(100, 50, -30)[1] == "Liquidating Assets"
    assert classify_capital_allocation(-100, 50, 30)[1] == "Distress Signal"
    assert classify_capital_allocation(-100, -50, 30)[1] == "Growth Funded by Debt"
    assert classify_capital_allocation(100, 50, 30)[1] == "Cash Accumulator"
    assert classify_capital_allocation(100, -50, -30, pat=50)[1] == "Shareholder Returns"
