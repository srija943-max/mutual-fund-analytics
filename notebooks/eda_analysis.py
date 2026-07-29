import pandas as pd

# Load CSV files
fund_master = pd.read_csv('data/raw/01_fund_master.csv')
transactions = pd.read_csv('data/raw/08_transactions.csv')

print("=== FUND MASTER OVERVIEW ===")
print(fund_master.head(3))

print("\n=== TRANSACTIONS OVERVIEW ===")
print(transactions.head(3))

print("\n=== MISSING VALUES IN TRANSACTIONS ===")
print(transactions.isnull().sum())

print("\n=== DATASET SUMMARY ===")
print(transactions.describe())