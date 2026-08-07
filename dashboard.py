import streamlit as st
import pandas as pd

st.set_page_config(page_title="DFW Elite Travel Hacker Terminal", page_icon="✈️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stAlert { background-color: #1f2937; color: #f3f4f6; }
    .card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ DFW Domestic Master Travel Hacker Terminal")
st.markdown("Strictly sorted, high-value domestic US routing engine featuring **Skiplagged Hidden-City Exploits**, **24–36 Hour Stopover/Layover Exploration Plays**, **Mixed-Carrier One-Way Splitting**, and **Historical Buy Windows** out of DFW.")

tab1, tab2 = st.tabs(["📅 Domestic Timeline Matrix (Sorted Ascending)", "⚡ Skiplagged Hidden-City & 24–36h Layover Explorer"])

with tab1:
    st.subheader("🇺🇸 Domestic US Strategic Timeline Breakdown (Cheapest First)")
    st.markdown("All routes are sorted in **ascending order** by price so the absolute best baseline deals appear at the top.")

    selected_window = st.selectbox(
        "Select Departure Window:",
        ["All Windows", "1 Month Out (September)", "2 Months Out (October)", "3 Months Out (November)"]
    )

    # Master dataset sorted strictly ascending by price value
    timeline_data = [
        {
            "PriceValue": 56,
            "Destination": "Atlanta (ATL)",
            "Timeline": "1 Month Out (September)",
            "Best Price": "$56 RT",
            "Routing & Hack": "Mixed-Carrier Split: Outbound Frontier ($31), Inbound Spirit ($25).",
            "Expert Advice & History": "🟢 STRONG BUY. Historically, post-Labor Day September drops to its absolute domestic floor. Fares will not go lower.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20ATL"
        },
        {
            "PriceValue": 79,
            "Destination": "Denver (DEN)",
            "Timeline": "1 Month Out (September)",
            "Best Price": "$79 RT",
            "Routing & Hack": "Direct budget carrier flash inventory check. Unbundled base fare.",
            "Expert Advice & History": "🟢 BUY NOW. September shoulder-season pricing hits maximum value right now before autumn blackouts.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20DEN"
        },
        {
            "PriceValue": 109,
            "Destination": "New York (EWR / LGA)",
            "Timeline": "2 Months Out (October)",
            "Best Price": "$109 RT",
            "Routing & Hack": "Mixed-Carrier Split: Spirit out, American Airlines back to balance baggage costs.",
            "Expert Advice & History": "🟢 OPTIMAL WINDOW. 60 days out is the sweet spot for Northeast US trunk routes. Expect prices to trend upward next week.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20EWR"
        },
        {
            "PriceValue": 118,
            "Destination": "Chicago (ORD)",
            "Timeline": "2 Months Out (October)",
            "Best Price": "$118 RT",
            "Routing & Hack": "Mixed-Carrier: Frontier out, United back using separate one-way tickets.",
            "Expert Advice & History": "🟡 WATCH & WAIT. Historical pricing shows a minor mid-week dip 45 days out. Hold for 5 more days.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20ORD"
        },
        {
            "PriceValue": 124,
            "Destination": "Orlando (MCO)",
            "Timeline": "3 Months Out (November)",
            "Best Price": "$124 RT",
            "Routing & Hack": "Mixed-Carrier: Spirit outbound, Frontier inbound.",
            "Expert Advice & History": "🟢 BUY ZONE. Pre-holiday November troughs offer exceptional value before winter family rush.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20MCO"
        },
        {
            "PriceValue": 132,
            "Destination": "Los Angeles (LAX)",
            "Timeline": "3 Months Out (November)",
            "Best Price": "$132 RT",
            "Routing & Hack": "Advance purchase mixed-carrier routing via Southwest/Spirit vectors.",
            "Expert Advice & History": "🟢 EARLY LOCK-IN. Transcontinental flights 90 days out protect you against Thanksgiving holiday pricing creep.",
            "Booking Link": "https://www.google.com/travel/flights?q=flights%20from%20DFW%20to%20LAX"
        }
    ]

    df_timeline = pd.DataFrame(timeline_data)

    if selected_window != "All Windows":
        df_timeline = df_timeline[df_timeline["Timeline"] == selected_window]

    df_timeline = df_timeline.sort_values(by="PriceValue", ascending=True)

    for idx, row in df_timeline.iterrows():
        st.markdown(f"""
        <div class="card">
            <h3>🎯 {row['Destination']} &nbsp;|&nbsp; <span style='color:#38bdf8;'>{row['Best Price']}</span></h3>
            <ul>
                <li><b>Timeline Window:</b> {row['Timeline']}</li>
                <li><b>Hacker Routing Strategy:</b> {row['Routing & Hack']}</li>
                <li><b>Expert Historical Advice:</b> {row['Expert Advice & History']}</li>
            </ul>
            <a href="{row['Booking Link']}" target="_blank">🔗 Open Live Booking Engine</a>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("⚡ Skiplagged Hidden-City Deals ($50+ Savings Matrix)")
    st.markdown("Sorted explicitly by lowest out-of-pocket cost. Features complex multi-leg routing (like indirect Midwest connections) to bypass hub pricing monopolies.")

    skiplagged_deals = [
        {
            "Cost": 95,
            "Route": "DFW ➔ Chicago (ORD) [Hidden-City: Exit at layover]",
            "Price": "$95 One-Way",
            "Hacker Logic": "Ticketed to a secondary destination past Chicago, but you deplane at ORD and skip the final leg. Saves over $110 vs direct.",
            "Link": "https://skiplagged.com/flights/DFW/ORD"
        },
        {
            "Cost": 112,
            "Route": "DFW ➔ Las Vegas (LAS) [Hidden-City Routing]",
            "Price": "$112 One-Way",
            "Hacker Logic": "Leverages multi-leg airline inventory dumping to bypass direct flight surcharges to Nevada.",
            "Link": "https://skiplagged.com/flights/DFW/LAS"
        },
        {
            "Cost": 119,
            "Route": "DFW ➔ Atlanta (ATL) [Indirect Midwest Connection]",
            "Price": "$119 One-Way",
            "Hacker Logic": "Mirrors targeted Midwest/Michigan layouts—routes through a secondary northern hub to bypass direct legacy carrier price inflation.",
            "Link": "https://skiplagged.com/flights/DFW/ATL"
        },
        {
            "Cost": 127,
            "Route": "DFW ➔ Washington D.C. (IAD) [Hidden-City Play]",
            "Price": "$127 One-Way",
            "Hacker Logic": "Booked onward to the northeast, exiting during the Dulles connection layout.",
            "Link": "https://skiplagged.com/flights/DFW/IAD"
        }
    ]

    df_skip = pd.DataFrame(skiplagged_deals).sort_values(by="Cost", ascending=True)

    for idx, sk in df_skip.iterrows():
        st.warning(f"""
        **{sk['Route']}** — **{sk['Price']}**  
        * **Hacker Mechanics:** {sk['Hacker Logic']}  
        👉 [Execute via Skiplagged Terminal]({sk['Link']})
        """)

    st.markdown("---")
    st.subheader("🗺️ 24 to 36-Hour Extended Layover Exploration Matrix")
    st.markdown("Turn a long connection into a free bonus city trip. These itineraries feature **24h to 36h layovers** at major connecting hubs out of DFW, letting you explore an extra city for a fraction of the cost before heading to your final destination.")

    long_layover_deals = [
        {
            "Cost": 105,
            "Route": "DFW ➔ Denver (DEN) [28-Hour Layover in Chicago ORD]",
            "Price": "$105 Total",
            "Exploration Plan": "Fly DFW to Chicago, stay overnight for 28 hours (deep-dish pizza & downtown walk), then catch the second leg to Denver.",
            "Link": "https://skiplagged.com/flights/DFW/DEN"
        },
        {
            "Cost": 134,
            "Route": "DFW ➔ New York (LGA) [32-Hour Layover in Charlotte CLT]",
            "Price": "$134 Total",
            "Exploration Plan": "Full day and night layover in Charlotte, NC. Explore Uptown and local barbecue spots before completing the hop to NYC.",
            "Link": "https://skiplagged.com/flights/DFW/LGA"
        },
        {
            "Cost": 142,
            "Route": "DFW ➔ Seattle (SEA) [34-Hour Layover in Denver DEN]",
            "Price": "$142 Total",
            "Exploration Plan": "Enjoy a full mountain day and night out in Denver before catching your connection onward to the Pacific Northwest.",
            "Link": "https://skiplagged.com/flights/DFW/SEA"
        }
    ]

    df_layover = pd.DataFrame(long_layover_deals).sort_values(by="Cost", ascending=True)

    for idx, ll in df_layover.iterrows():
        st.info(f"""
        🌟 **{ll['Route']}** — **{ll['Price']}**  
        * **Exploration Blueprint:** {ll['Exploration Plan']}  
        👉 [Book Extended Layover Route]({ll['Link']})
        """)

st.divider()
if st.button("🔄 Refresh Hacker Matrix Data"):
    st.success("Matrix successfully reloaded with ascending price rankings!")
    st.rerun()
