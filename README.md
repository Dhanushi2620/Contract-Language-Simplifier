# 📄 Contract Language Simplifier (CLS)

An AI-powered web application that simplifies complex legal or contract language into clear, easy-to-understand text.  
Built using **Streamlit**, **Hugging Face Transformers**, and **OpenAI API**, the system performs **text simplification, summarization, and readability analysis**.

---

## 🚀 Features

### 🔐 User Authentication
- Secure sign-up, sign-in, and password recovery (JWT + bcrypt encryption)
- User-specific session management with SQLite backend

### 🧠 Text Analysis
- Upload contracts in **PDF, DOCX, or TXT** format
- Calculates readability metrics: *Flesch-Kincaid Grade* & *Gunning Fog Index*
- Generates top keywords and complexity analysis

### ✍️ Simplification & Summarization
- AI-based simplification using **FLAN-T5** and **BART** models
- Side-by-side comparison of original vs. simplified text
- Adjustable simplification levels — *Basic*, *Intermediate*, and *Advanced*

### 📚 Legal Term Glossary
- Built-in glossary explaining key legal terms such as “Agreement”, “Liability”, “Obligation”, etc.

### 🖥️ Admin Dashboard
- Monitor simplification requests, user activity, and system performance
- Manage glossary or review AI outputs (future-ready)

### ☁️ Deployment Ready
- Fully containerized for deployment using **Streamlit Cloud**, **Hugging Face Spaces**, or **Docker**

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **Backend** | Python |
| **Database** | SQLite |
| **AI / NLP Models** | FLAN-T5, BART-large-cnn |
| **Authentication** | JWT, bcrypt |
| **Environment Management** | venv |
| **Styling** | Custom CSS (modern, minimalist white-blue theme) |

---

## 🧰 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/contract-language-simplifier.git
cd contract-language-simplifier

2️⃣ Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate     # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)
