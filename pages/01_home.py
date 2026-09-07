import streamlit as st
from src.dashboard.utils.db import get_companies, get_ratios
st.title("Executive Overview")
comps = get_companies()
st.metric("Total Companies", len(comps))
st.dataframe(comps[['company_name', 'sector']].head(10))
