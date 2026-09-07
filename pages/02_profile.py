import streamlit as st
from src.dashboard.utils.db import get_companies, get_ratios
st.title("Company Profile")
ticker = st.selectbox("Select Ticker", get_companies()['ticker'].tolist())
st.dataframe(get_ratios(ticker))
