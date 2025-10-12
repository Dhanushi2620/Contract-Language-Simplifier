import streamlit as st
from transformers import pipeline
import re
import docx2txt
import PyPDF2
from nltk.tokenize import sent_tokenize
import nltk

# ====== DOWNLOAD NLTK DATA ======
nltk.download('punkt', quiet=True)

# ====== PAGE CONFIG ======
st.set_page_config(page_title="Simplify Contracts", layout="wide")

# ====== STYLING ======
st.markdown("""
    <style>
        body { background-color: #f1f5fb; color: #1b1b1b; font-family: 'Segoe UI', sans-serif; }
        .header { font-size: 30px; font-weight: 700; text-align: center; color: #1e3a5f; margin-bottom: 10px; }
        .subtext { font-size: 16px; text-align: center; color: #3a3a3a; margin-bottom: 30px; }
        .card { background-color: white; padding: 20px; border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .stButton>button { background-color: #1e3a5f; color: white; border-radius: 6px;
                            font-weight: 600; border: none; padding: 10px 20px; }
        .stButton>button:hover { background-color: #365985; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header'>Contract Simplification Tool</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Upload or paste your legal text to simplify it intelligently using AI.</div>", unsafe_allow_html=True)

# ====== LOAD SIMPLIFICATION MODEL ======
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")
model = load_model()

# ====== FILE UPLOAD ======
st.markdown("<div class='card'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload contract (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

text = ""
if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext == "pdf":
        pdf = PyPDF2.PdfReader(uploaded_file)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    elif ext == "docx":
        text = docx2txt.process(uploaded_file)
    elif ext == "txt":
        text = uploaded_file.read().decode("utf-8")
    st.success(f"Extracted text from {ext.upper()} file successfully.")
else:
    text = st.text_area("Or paste your contract text here:", height=200)
st.markdown("</div>", unsafe_allow_html=True)

# ====== SIMPLIFICATION FUNCTION ======
def simplify_text(long_text):
    """Split long text into sentences, simplify each part, and join them."""
    sentences = sent_tokenize(long_text)
    simplified_sentences = []
    for sent in sentences:
        result = model(sent, max_length=100, num_return_sequences=1)[0]['generated_text']
        simplified_sentences.append(result)
    return " ".join(simplified_sentences)

# ====== SIMPLIFY BUTTON ======
if st.button("Simplify Contract"):
    if not text.strip():
        st.warning("Please upload or paste contract text first.")
    else:
        with st.spinner("Simplifying contract text..."):
            simplified_text = simplify_text(text)

        # ====== DISPLAY OUTPUT ======
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Text")
            st.markdown(text)
        with col2:
            st.subheader("Simplified Text")
            st.markdown(simplified_text)

        st.download_button(
            label="Download Simplified Text",
            data=simplified_text,
            file_name="simplified_contract.txt",
            mime="text/plain"
        )
