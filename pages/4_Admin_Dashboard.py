import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime, timedelta

# =============================
# PAGE CONFIG & STYLE
# =============================
st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.markdown("""
    <style>
        body { background-color: #f1f5fb; color: #1b1b1b; font-family: 'Segoe UI', sans-serif; }
        .header { font-size: 30px; font-weight: 700; text-align: center; color: #1e3a5f; margin-bottom: 10px; }
        .subtext { font-size: 16px; text-align: center; color: #3a3a3a; margin-bottom: 30px; }
        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            text-align: center;
        }
        .metric-value {
            font-size: 26px;
            font-weight: 700;
            color: #1e3a5f;
        }
        .metric-label {
            color: #555;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header'> Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Monitor simplification activity, performance metrics, and glossary management.</div>", unsafe_allow_html=True)

# =============================
# SIMULATED DATA (Replace with DB later)
# =============================
dates = [datetime.now() - timedelta(days=i) for i in range(10)]
activity_data = {
    "Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Simplifications": [random.randint(5, 25) for _ in dates],
    "Users Active": [random.randint(3, 15) for _ in dates],
    "Avg Processing Time (s)": [round(random.uniform(1.5, 4.5), 2) for _ in dates]
}
df_activity = pd.DataFrame(activity_data)

# =============================
# METRIC CARDS
# =============================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='metric-card'><div class='metric-value'>324</div><div class='metric-label'>Total Simplifications</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><div class='metric-value'>82%</div><div class='metric-label'>User Satisfaction</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><div class='metric-value'>2.3s</div><div class='metric-label'>Avg Response Time</div></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='metric-card'><div class='metric-value'>98%</div><div class='metric-label'>System Uptime</div></div>", unsafe_allow_html=True)

# =============================
# ACTIVITY OVER TIME
# =============================
st.markdown("### Simplification Requests Over Time")
st.line_chart(df_activity.set_index("Date")[["Simplifications", "Users Active"]])

# =============================
# PERFORMANCE STATS TABLE
# =============================
st.markdown("### System Performance Logs")
st.dataframe(df_activity, use_container_width=True)

# =============================
# GLOSSARY MANAGEMENT SECTION
# =============================
st.markdown("### Manage Legal Glossary")
default_glossary = {
    "Agreement": "A mutual understanding between parties about their responsibilities.",
    "Confidentiality": "Keeping sensitive information secret.",
    "Termination": "Ending the contract before it naturally expires."
}

if "glossary" not in st.session_state:
    st.session_state.glossary = default_glossary

glossary = st.session_state.glossary

colA, colB = st.columns(2)
with colA:
    new_term = st.text_input("Add a new term:")
with colB:
    new_meaning = st.text_input("Add definition:")

if st.button("➕ Add Term"):
    if new_term and new_meaning:
        glossary[new_term.capitalize()] = new_meaning
        st.success(f"Added term: {new_term.capitalize()}")
        time.sleep(0.5)
        st.rerun()
    else:
        st.warning("Please fill both fields before adding a term.")

st.write("#### Current Glossary")
for term, meaning in glossary.items():
    st.markdown(f"**{term}** → {meaning}")

# =============================
# EXPORT OPTION
# =============================
st.markdown("---")
st.download_button(
    label="⬇ Download Activity Report (CSV)",
    data=df_activity.to_csv(index=False),
    file_name="simplification_activity_report.csv",
    mime="text/csv"
)
