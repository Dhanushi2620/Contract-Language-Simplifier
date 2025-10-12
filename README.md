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
```
### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

```
### 3️⃣ Install Dependencies
```bash 
pip install -r requirements.txt

```
### 4️⃣ Set up OpenAI API Key
```bash 
Create a .streamlit/secrets.toml file in your project directory and add the following:

OPENAI_API_KEY = "your-api-key-here"
```
### 5️⃣ Run the Application
```bash 
streamlit run app.py

```
# 📊 Project Milestones

Milestone 1: User Authentication (Login, Signup, JWT-based Security)

Milestone 2: Text Analysis and Readability Metrics Integration

Milestone 3: Contract Simplification with AI-Powered Text Generation

Milestone 4: Multi-Level Simplification and Admin Dashboard


# 🔮 Future Enhancements

Dynamic glossary generation using AI

Real-time feedback and rating system

Integration with document management APIs (Google Drive, DocuSign)

Fine-tuning model on Indian legal datasets

Cloud-based user analytics dashboard

# 👩‍💻 Developer

Dhanushi Gupta
B.Tech (CSE) | Machine Learning & AI Enthusiast
📧 [dhanushi.ug23@nsut.ac.in
]

Arnav Gupta
B.Tech (CSE) | AI Enthusiast
📧 [2k22.csiot.2212865@gmail.com
]
