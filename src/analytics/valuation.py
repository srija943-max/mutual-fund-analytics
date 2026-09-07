import pandas as pd
import numpy as np

def compute_valuation_metrics(df):
    df['FCF_yield_pct'] = np.where(df['market_cap_cr'] > 0, (df['free_cash_flow_cr'] / df['market_cap_cr']) * 100, 0.0).round(2)
    sector_medians = df.groupby('sector')['pe_ratio'].transform('median')
    df['PE_vs_sector_median_pct'] = (((df['pe_ratio'] - sector_medians) / sector_medians) * 100).round(2)
    
    conditions = [
        df['pe_ratio'] > (sector_medians * 1.5),
        df['pe_ratio'] < (sector_medians * 0.7)
    ]
    choices = ['Caution', 'Discount']
    df['flag'] = np.select(conditions, choices, default='Fair')
    return df
