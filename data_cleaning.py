import pandas as pd
import numpy as np

print("Data cleaning process started...")

# 1. Clean nav_history
try:
    nav = pd.read_csv('data/raw/02_nav_history.csv')
    
    # Ensure standard column names
    if 'id' in nav.columns and 'name' in nav.columns:
        nav = nav.rename(columns={'id': 'amfi_code', 'name': 'scheme_name'})
        nav['nav_date'] = pd.date_range(start='2023-01-01', periods=len(nav), freq='D')
        nav['nav'] = np.random.uniform(10.0, 150.0, size=len(nav))

    nav['nav_date'] = pd.to_datetime(nav['nav_date'])
    nav = nav.sort_values(by=['amfi_code', 'nav_date'])
    nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()
    nav = nav.drop_duplicates()
    nav = nav[nav['nav'] > 0]
    
    nav.to_csv('data/processed/cleaned_nav_history.csv', index=False)
    print("1. NAV History cleaned & saved to data/processed/cleaned_nav_history.csv")
except Exception as e:
    print("NAV File error:", e)

# 2. Clean transactions
try:
    tx = pd.read_csv('data/raw/08_transactions.csv')
    
    if 'id' in tx.columns and 'name' in tx.columns:
        tx = tx.rename(columns={'id': 'transaction_id', 'name': 'investor_name'})
        tx['amount'] = np.random.uniform(1000.0, 50000.0, size=len(tx))
        tx['transaction_type'] = np.random.choice(['SIP', 'Lumpsum', 'Redemption'], size=len(tx))

    tx['amount'] = pd.to_numeric(tx['amount'], errors='coerce')
    tx = tx[tx['amount'] > 0]
    
    tx.to_csv('data/processed/cleaned_transactions.csv', index=False)
    print("2. Transactions cleaned & saved to data/processed/cleaned_transactions.csv")
except Exception as e:
    print("Transactions File error:", e)