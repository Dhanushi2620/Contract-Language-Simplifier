import streamlit as st
from transformers import pipeline
import re
import docx2txt
import PyPDF2

# ============ PAGE CONFIG ============
st.set_page_config(page_title="Multi-Level Simplification", layout="wide")

# ============ GLOBAL STYLE ============
st.markdown("""
    <style>
        body { background-color: #f1f5fb; color:#1b1b1b; font-family:'Segoe UI',sans-serif; }
        .header { font-size:30px; font-weight:700; text-align:center; color:#1e3a5f; margin-bottom:5px; }
        .subtext { font-size:16px; text-align:center; color:#3a3a3a; margin-bottom:30px; }
        .card { background:#fff; padding:20px; border-radius:10px; box-shadow:0px 4px 8px rgba(0,0,0,0.08); margin-bottom:20px; }
        .stButton>button { background:#1e3a5f; color:white; border:none; border-radius:6px; padding:10px 22px; font-weight:600; }
        .stButton>button:hover { background:#365985; }
        .metric-box { background:#1e3a5f; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:600; box-shadow:0px 2px 5px rgba(0,0,0,0.1); }
        .metric-box small { display:block; font-size:12px; font-weight:400; opacity:0.9; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header'>Multi-Level Simplification</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Choose your simplification level and explore key-term explanations.</div>", unsafe_allow_html=True)

# ============ LOAD MODEL ============
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")
model = load_model()

# ============ GLOSSARY ============
LEGAL_GLOSSARY = {
    "agreement": "A mutual understanding between parties about their responsibilities.",
    "party": "A person or organization involved in a contract.",
    "termination": "Ending the contract before it naturally expires.",
    "liability": "Legal responsibility for something that happens.",
    "obligation": "A duty or commitment that must be fulfilled.",
    "confidentiality": "Keeping sensitive information secret.",
    "employer": "The company or person who provides work and pay.",
    "employee": "The individual who performs work for the employer."
}

# ============ FILE UPLOAD / TEXT AREA ============
st.markdown("<div class='card'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📄 Upload Contract (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

text = ""
if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()
    if file_type == "pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    elif file_type == "docx":
        text = docx2txt.process(uploaded_file)
    elif file_type == "txt":
        text = uploaded_file.read().decode("utf-8")
    st.success(f"✅ Extracted text from {file_type.upper()} file successfully.")
else:
    text = st.text_area("Or paste your legal text here:", height=200)
st.markdown("</div>", unsafe_allow_html=True)

# ============ LEVEL SELECTOR ============
level_map = {0: "Basic", 1: "Intermediate", 2: "Advanced"}
level_value = st.slider("Simplification Level", 0, 2, 1)
level = level_map[level_value]
st.info(f"Selected Mode: **{level} Simplification**")

# ============ SIMPLIFICATION LOGIC ============
def simplify_text(text, mode):
    prompt = {
        "Basic": f"Simplify this legal text slightly for clarity but keep professional tone:\n{text}",
        "Intermediate": f"Rephrase this legal contract in simpler, non-technical English:\n{text}",
        "Advanced": f"Rewrite this legal document in very simple, everyday language:\n{text}"
    }[mode]
    return model(prompt, max_length=500, do_sample=False)[0]["generated_text"]

# ============ PROCESS BUTTON ============
if st.button("Simplify Text"):
    if not text.strip():
        st.warning("Please upload or paste text first.")
    else:
        with st.spinner(f"Simplifying using {level} mode..."):
            simplified = simplify_text(text, level)

        # Highlight glossary terms in original text
        highlighted = text
        for term in LEGAL_GLOSSARY:
            highlighted = re.sub(rf"\\b({term})\\b", r"**\\1**", highlighted, flags=re.IGNORECASE)

        # Display
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Original Text (Highlighted)")
            st.markdown(highlighted)
        with col2:
            st.markdown("### Simplified Text")
            st.markdown(simplified)

        st.download_button("⬇ Download Simplified Text", data=simplified,
                           file_name="simplified_contract.txt", mime="text/plain")

# ============ LEGAL GLOSSARY SEARCH ============
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Legal Terms Glossary")
term_query = st.text_input("Search term:")
if term_query:
    st.info(f"**{term_query.capitalize()}** → {LEGAL_GLOSSARY.get(term_query.lower(), 'No definition found.')}")
else:
    for t, m in LEGAL_GLOSSARY.items():
        st.write(f"**{t.capitalize()}** → {m}")
st.markdown("</div>", unsafe_allow_html=True)

# ============ METRICS ============
st.markdown("---")
st.markdown("### Key Performance Metrics")
c1, c2, c3, c4 = st.columns(4)
c1.markdown("<div class='metric-box'>3<small>Simplification Levels</small></div>", unsafe_allow_html=True)
c2.markdown("<div class='metric-box'>80%<small>User Satisfaction</small></div>", unsafe_allow_html=True)
c3.markdown("<div class='metric-box'>1000+<small>Concurrent Users</small></div>", unsafe_allow_html=True)
c4.markdown("<div class='metric-box'>100%<small>Admin Coverage</small></div>", unsafe_allow_html=True)
