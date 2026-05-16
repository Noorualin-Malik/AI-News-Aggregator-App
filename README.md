# 🚀 Real-Time AI News Lead Aggregator

An AI-powered microservice/web application that fetches real-time technology and business news, analyzes articles using Gemini AI, identifies businesses facing technical or operational challenges, and stores actionable leads in SQLite.

---

# 📌 Project Objective

This application:

- Fetches real-time tech/business news
- Uses an LLM (Gemini AI) to analyze articles
- Detects businesses facing:
  - Technical failures
  - Operational bottlenecks
  - AI automation needs
  - Digital transformation challenges
- Stores high-value leads in SQLite
- Displays results using Streamlit

---

# 🛠️ Tech Stack

- Python
- Streamlit
- SQLite
- Gemini API
- NewsAPI
- dotenv

---

# 📂 Folder Structure

```bash
ai-news-lead-aggregator/
│
├── app.py
├── fetch_news.py
├── filter_news.py
├── database.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── leads.db
│
└── utils/
    └── prompts.py