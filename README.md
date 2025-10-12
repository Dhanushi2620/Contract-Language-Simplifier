# Contract Language Simplifier — Milestone 1 (Streamlit)

This starter delivers Weeks 1–2:
- Sign Up / Sign In (JWT)
- Profile + Change Password
- Document paste/upload and save
- SQLite persistence

## Quickstart

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt

# set env
copy .env.example .env   # Windows PowerShell: copy .env.example .env
# macOS/Linux: cp .env.example .env
# open .env and put a long random JWT secret

streamlit run app.py
```

Open http://localhost:8501

## Generate a strong secret
```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

## Notes
- DB file: `cls_app.db`
- To reset: delete `cls_app.db` (you will lose users and docs)
- Do not commit `.env` or `cls_app.db` to public repos
