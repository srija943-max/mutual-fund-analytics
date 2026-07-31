import sqlite3
import pandas as pd
from sqlalchemy import create_engine

print("Building SQLite Database Pipeline...")

# 1. Connect and create SQLite DB engine
engine = create_engine('sqlite:///bluestock_mf.db')

# 2. Read cleaned datasets from data/processed/
nav_df = pd.read_csv('data/processed/cleaned_nav_history.csv')
tx_df = pd.read_csv('data/processed/cleaned_transactions.csv')

# 3. Load DataFrames directly into SQLite Tables
nav_df.to_sql('fact_nav', con=engine, if_exists='replace', index=False)
tx_df.to_sql('fact_transactions', con=engine, if_exists='replace', index=False)

print("Data successfully loaded into bluestock_mf.db!")