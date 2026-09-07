import streamlit as st
from src.dashboard.utils.db import get_ratios
st.title("Screener Engine")
df = get_ratios()
min_roe = st.sidebar.slider("Min ROE (%)", 0.0, 50.0, 15.0)
filtered = df[df['return_on_equity_pct'] >= min_roe]
st.write(f"Matches: {len(filtered)}")
st.dataframe(filtered[['ticker', 'company_name', 'return_on_equity_pct']])
st.download_button("Download CSV", filtered.to_csv(index=False), "screener_results.csv")
