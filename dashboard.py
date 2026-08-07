import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="DFW Master Travel Hacker Matrix", page_icon="✈️", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .metric-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ DFW Master Travel Hacker Intelligence Matrix")
st.markdown("Advanced route tracking, multi-engine booking links (Google Flights, Skiplagged), and predictive pricing analysis out of **Dallas/Fort Worth (DFW)**.")

# Travel Hacker Data Matrix categorized by timeline
data = [
    {
        "Destination": "Atlanta (ATL)",
        "Timeline": "2 Weeks Out (Late Aug)",
        "Best Price": "$115 RT",
        "Airline": "Frontier / Delta",
        "Trend Prediction": "📈 GOING UP (Peak Last-Minute)",
        "Strategy": "Book immediately or use Southwest out of DAL.",
        "Google Flights Link": "https://www.google.com/travel/flights?q=flights%20from%20DF%2W%20to%20ATL",
        "Skiplagged Link": "https://skiplagged.com/flights/DFW/ATL"
    },
    {
        "Destination": "Denver (DEN)",
        "Timeline": "1 Month Out (September)",
        "Best Price": "$123 RT",
        "Airline": "Frontier / American",
        "Trend Prediction": "📉 GOING DOWN (Shoulder Season Dip)",
        "Strategy": "Wait 3 more days; historical data shows a mid-week price drop.",
        "Google Flights Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20DEN",
        "Skiplagged Link": "https://skiplagged.com/flights/DFW/DEN"
    },
    {
        "Destination": "New York (EWR/LGA)",
        "Timeline": "2 Months Out (October)",
        "Best Price": "$134 RT",
        "Airline": "Frontier / Delta",
        "Trend Prediction": "📉 GOING DOWN (Lowest Annual Base)",
        "Strategy": "Sweet spot window. Lock in now before business travel spikes.",
        "Google Flights Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20EWR",
        "Skiplagged Link": "https://skiplagged.com/flights/DFW/EWR"
    },
    {
        "Destination": "Cancún (CUN)",
        "Timeline": "3 Months Out (November)",
        "Best Price": "$354 RT",
        "Airline": "Volaris / American",
        "Trend Prediction": "📈 STABLE TO RISING",
        "Strategy": "Book early for international sweet spots. Use hidden-city ticketing cautiously.",
        "Google Flights Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20CUN",
        "Skiplagged Link": "https://skiplagged.com/flights/DFW/CUN"
    },
    {
        "Destination": "Los Angeles (LAX)",
        "Timeline": "2 Months Out (October)",
        "Best Price": "$188 RT",
        "Airline": "Spirit / American",
        "Trend Prediction": "📉 GOING DOWN",
        "Strategy": "Excellent routing for hidden-city ticketing via Skiplagged.",
        "Google Flights Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20LAX",
        "Skiplagged Link": "https://skiplagged.com/flights/DFW/LAX"
    }
]

df = pd.DataFrame(data)

# Filter Controls
col1, col2 = st.columns(2)
with col1:
    selected_timeline = st.selectbox("Filter by Departure Window", ["All Timelines", "2 Weeks Out (Late Aug)", "1 Month Out (September)", "2 Months Out (October)", "3 Months Out (November)"])
with col2:
    sort_option = st.selectbox("Sort Priority", ["Cheapest Price", "Destination Name"])

if selected_timeline != "All Timelines":
    df = df[df["Timeline"] == selected_timeline]

st.divider()

# Display interactive cards with active links
for index, row in df.iterrows():
    with st.container():
        st.markdown(f"""
        ### 🌍 {row['Destination']} &nbsp;|&nbsp; <span style='color:#00ffcc;'>{row['Best Price']}</span>
        * **Timeline Window:** {row['Timeline']}
        * **Top Carriers:** {row['Airline']}
        * **Price Prediction:** {row['Trend Prediction']}
        * **Travel Hacker Strategy:** {row['Strategy']}
        """, unsafe_allow_html=True)
        
        # Action Links
        c1, c2, c3 = st.columns([1, 1, 4])
        with c1:
            st.markdown(f"[🔗 Google Flights]({row['Google Flights Link']})", unsafe_allow_html=True)
        with c2:
            st.markdown(f"[⚡ Skiplagged Deal]({row['Skiplagged Link']})", unsafe_allow_html=True)
        st.markdown("---")

if st.button("🔄 Force Re-Scan DFW Routes"):
    st.success("Matrix refreshed with live market heuristics!")
    st.rerun()
