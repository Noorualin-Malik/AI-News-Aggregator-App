Project Objective

This application:

Fetches real-time tech/business news
Uses an LLM (Gemini AI) to analyze articles
Detects businesses facing:
Technical failures
Operational bottlenecks
AI automation needs
Digital transformation challenges
Stores high-value leads in SQLite
Displays results using Streamlit UI in real-time

🛠️ Tech Stack
Python
Streamlit
SQLite
Gemini API
NewsAPI
python-dotenv
📂 Folder Structure
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

    
⚙️ How It Works (System Flow)
The system works in 5 steps:
1️⃣ News Fetching
NewsAPI fetches latest tech/business articles
2️⃣ Data Preprocessing
Extracts:
Title
Description
Source
URL
3️⃣ AI Analysis (Gemini)
Each article is sent to Gemini AI
Prompt checks:
Technical failure
Operational issue
Automation need
4️⃣ Filtering
If article is relevant → marked as HIGH-VALUE LEAD
If not → ignored
5️⃣ Storage + UI
High-value leads stored in SQLite
Streamlit displays:
Live analysis
Saved leads
Article links

▶️ How to Run This Project
1️⃣ Clone Repository
git clone <your-repo-link>
cd ai-news-lead-aggregator
2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup API Keys

Create a .env file in root directory:
NEWS_API_KEY=your_news_api_key
GEMINI_API_KEY=your_gemini_api_key
Run Application
streamlit run app.py
Output (What You Will See)

When you run the app:
Step 1: Click Button
"Fetch & Analyze News"
Step 2: Live Processing
You will see:
Article title
Description
AI analysis (YES / NO)
Status:
✅ High-Value Lead Found
❌ Not Relevant
Step 3: Results Section
At the bottom:
Total leads saved
List of saved leads
Clickable article links
Data Storage (SQLite)
All high-value leads are stored in:
data/leads.db
Each record contains:
Title
Description
Source
URL
🔐 Security
API keys stored in .env
.env excluded using .gitignore
No credentials exposed on GitHub
