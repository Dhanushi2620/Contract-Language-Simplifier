import streamlit as st
import sqlite3
from passlib.hash import bcrypt
from datetime import datetime
import time

# =============================
# PAGE CONFIGURATION
# =============================
st.set_page_config(page_title="Contract Simplifier", page_icon="📘", layout="wide")

# =============================
# DATABASE SETUP
# =============================
DB_PATH = "cls_app.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

init_db()

# =============================
# UTILITY FUNCTIONS
# =============================
def create_user(name, email, password):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
                    (name, email, bcrypt.hash(password), datetime.utcnow().isoformat()))
        conn.commit()
        return True, None
    except sqlite3.IntegrityError:
        return False, "Email already exists."
    finally:
        conn.close()

def verify_user(email, password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, password_hash FROM users WHERE email=?", (email,))
    user = cur.fetchone()
    conn.close()
    if user and bcrypt.verify(password, user[3]):
        return {"id": user[0], "name": user[1], "email": user[2]}
    return None

def reset_password(email, new_password):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE users SET password_hash=? WHERE email=?", (bcrypt.hash(new_password), email))
    conn.commit()
    conn.close()

# =============================
# PAGE STYLING
# =============================
st.markdown("""
    <style>
        body {background-color: #f1f5fb; color: #1b1b1b; font-family: 'Segoe UI', sans-serif;}
        .header {font-size: 32px; font-weight: bold; text-align: center; color: #1e3a5f; margin-bottom: 10px;}
        .subtext {text-align: center; color: #3a3a3a; margin-bottom: 30px;}
        .stButton>button {
            background-color: #1e3a5f;
            color: white;
            border-radius: 6px;
            font-weight: 600;
            padding: 10px 20px;
            border: none;
        }
        .stButton>button:hover {background-color: #365985;}
        .card {
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            width: 400px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# =============================
# AUTHENTICATION LOGIC
# =============================
if "page" not in st.session_state:
    st.session_state.page = "login"

st.markdown("<div class='header'>Contract Language Simplifier</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Simplify legal contracts using AI — Log in to continue.</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if st.session_state.page == "login":
    st.subheader("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Login"):
            user = verify_user(email, password)
            if user:
                st.session_state.user = user
                st.success(f"Welcome {user['name']}!")
                time.sleep(1)
                st.switch_page("pages/1_Simplify.py")
            else:
                st.error("Invalid email or password.")
    with c2:
        if st.button("Create Account"):
            st.session_state.page = "signup"
            st.rerun()

    if st.button("Forgot Password?"):
        st.session_state.page = "forgot"
        st.rerun()

elif st.session_state.page == "signup":
    st.subheader("Create Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if not name or not email or not password:
            st.warning("All fields are required.")
        elif password != confirm:
            st.error("Passwords do not match.")
        else:
            ok, msg = create_user(name, email, password)
            if ok:
                st.success("Account created successfully! Please log in.")
                time.sleep(1)
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error(msg)

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

elif st.session_state.page == "forgot":
    st.subheader("Reset Password")
    email = st.text_input("Enter your registered email")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm New Password", type="password")

    if st.button("Reset Password"):
        if not email or not new_password:
            st.warning("Please fill all fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            reset_password(email, new_password)
            st.success("Password reset successfully! Please log in.")
            time.sleep(1)
            st.session_state.page = "login"
            st.rerun()

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
