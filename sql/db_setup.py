import pandas as pd
import sqlite3

# 1. Database Connection Create Cheyadam
conn = sqlite3.connect('mutual_fund.db')
cursor = conn.cursor()

print("=== 1. CREATING DATABASE & LOADING DATA ===")

# 2. CSV Files ni SQLite Tables ga Load Cheyadam
fund_master = pd.read_csv('data/raw/01_fund_master.csv')
transactions = pd.read_csv('data/raw/08_transactions.csv')

fund_master.to_sql('fund_master', conn, if_exists='replace', index=False)
transactions.to_sql('transactions', conn, if_exists='replace', index=False)

print("Tables 'fund_master' and 'transactions' loaded successfully!")

# 3. SQL Query 1: Display Top 5 Fund Master Records
print("\n=== 2. SQL QUERY: SELECT TOP 5 FUNDS ===")
query1 = "SELECT * FROM fund_master LIMIT 5;"
df_funds = pd.read_sql_query(query1, conn)
print(df_funds)

# 4. SQL Query 2: Transactions Summary
print("\n=== 3. SQL QUERY: TRANSACTIONS COUNT ===")
query2 = "SELECT COUNT(*) as total_transactions FROM transactions;"
df_trans = pd.read_sql_query(query2, conn)
print(df_trans)

# Connection Close
conn.close()
print("\nDatabase processing completed successfully!")