import sqlite3
import pandas as pd
import streamlit as st

@st.cache_data(ttl=600)
def get_companies():
    conn = sqlite3.connect("nifty100.db")
    df = pd.read_sql_query("SELECT * FROM companies", conn)
    conn.close()
    return df

@st.cache_data(ttl=600)
def get_ratios(ticker=None):
    conn = sqlite3.connect("nifty100.db")
    q = "SELECT c.ticker, c.company_name, c.sector, r.* FROM financial_ratios r JOIN companies c ON c.company_id = r.company_id"
    if ticker:
        q += f" WHERE c.ticker = '{ticker}'"
    df = pd.read_sql_query(q, conn)
    conn.close()
    return df
