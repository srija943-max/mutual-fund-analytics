def validate_data_quality(df_companies, df_pnl, df_bs):
    failures = []
    # DQ-01 PK Uniqueness
    if df_companies['company_id'].duplicated().any():
        failures.append({"rule": "DQ-01", "severity": "CRITICAL", "desc": "Duplicate Company IDs"})
    # DQ-06 Positive Sales
    if (df_pnl['sales'] <= 0).any():
        failures.append({"rule": "DQ-06", "severity": "WARNING", "desc": "Zero or negative sales found"})
    return failures
