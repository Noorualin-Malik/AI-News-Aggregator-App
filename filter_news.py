import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
You are an AI business analyst.

Analyze this article carefully.

Determine whether the company/business is facing:
- technical failure
- operational bottleneck
- automation need
- cyberattack
- digital transformation issue
- workflow inefficiency

Reply ONLY with:
YES
or
NO
"""

def filter_article(article):

    content = f"""
    Title: {article['title']}

    Description:
    {article['description']}
    """

    try:

        response = model.generate_content(
            PROMPT + content
        )

        answer = response.text.strip().upper()

        print("Gemini Response:", answer)

        if answer.startswith("YES"):
            return True

        return False

    except Exception as e:

        print("Gemini Error:", e)

        return False