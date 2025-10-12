import streamlit as st

# =============================
# PAGE CONFIGURATION
# =============================
st.set_page_config(page_title="Admin Dashboard", layout="wide")

# =============================
# STYLING
# =============================
st.markdown("""
    <style>
        body {
            background-color:#f1f5fb;
            font-family:'Segoe UI';
            color:#1e3a5f;
        }
        .header {
            font-size:28px;
            font-weight:700;
            text-align:center;
            margin-bottom:30px;
        }
        .metric {
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0px 2px 6px rgba(0,0,0,0.1);
            text-align:center;
        }
        .metric h3 {
            font-size:26px;
            margin:0;
            color:#1e3a5f;
        }
        .metric p {
            margin:5px 0 0 0;
            color:#3a3a3a;
        }
    </style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.markdown("<div class='header'>Admin Dashboard — Simplification Insights</div>", unsafe_allow_html=True)

# =============================
# METRICS DISPLAY
# =============================
col1, col2, col3 = st.columns(3)
col1.markdown("<div class='metric'><h3>1,000+</h3><p>Active Users</p></div>", unsafe_allow_html=True)
col2.markdown("<div class='metric'><h3>92%</h3><p>Successful Simplifications</p></div>", unsafe_allow_html=True)
col3.markdown("<div class='metric'><h3>1.8s</h3><p>Avg Response Time</p></div>", unsafe_allow_html=True)

# =============================
# ADDITIONAL INFO
# =============================
st.markdown("---")
st.subheader("System Overview")
st.write("""
This dashboard provides insights into user engagement, model performance, and system health.  
It can be expanded to include:
- Simplification logs and statistics  
- Model usage frequency  
- Average document size processed  
- User feedback and satisfaction scores  
""")
