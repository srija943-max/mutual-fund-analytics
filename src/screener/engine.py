def apply_screener(df, preset_name):
    if preset_name == "Quality Compounder":
        return df[(df['return_on_equity_pct'] > 15) & (df['debt_to_equity'] < 1.0) & (df['free_cash_flow_cr'] > 0)]
    elif preset_name == "Value Pick":
        return df[(df['debt_to_equity'] < 2.0) & (df['dividend_payout_ratio_pct'] > 15)]
    elif preset_name == "Growth Accelerator":
        return df[(df['revenue_cagr_5yr'] > 12) & (df['pat_cagr_5yr'] > 15)]
    elif preset_name == "Dividend Champion":
        return df[(df['dividend_payout_ratio_pct'] <= 80) & (df['free_cash_flow_cr'] > 0)]
    elif preset_name == "Debt-Free Blue Chip":
        return df[(df['debt_to_equity'] == 0) & (df['return_on_equity_pct'] > 12)]
    else:
        return df[(df['revenue_cagr_5yr'] > 10) & (df['free_cash_flow_cr'] > 0)]
