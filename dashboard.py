import streamlit as st
import json
import os

st.set_page_config(page_title="DFW Flight Deals", page_icon="✈️", layout="centered")

st.title("✈️ DFW Live Flight Deals Tracker")
st.markdown("Your automated tracker scanning cheap flights out of Dallas/Fort Worth.")

data_path = "data/deals.json"

if os.path.exists(data_path):
    with open(data_path, "r") as f:
        deals = json.load(f)
    
    if deals:
        st.success(f"Loaded {len(deals)} active flight deals!")
        # Display as a clean interactive table
        st.dataframe(deals, use_container_width=True)
    else:
        st.warning("No deals currently listed in the database.")
else:
    st.info("Waiting for the background script to run and generate flight data...")

if st.button("🔄 Refresh Data"):
    st.rerun()
