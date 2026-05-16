import requests
import os


NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news():

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=system failure OR operational issue OR AI automation OR cyberattack OR business outage"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=10"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching news")
        return []

    data = response.json()

    articles = data.get("articles", [])

    news_list = []

    for article in articles:

        news_list.append({
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "url": article.get("url", ""),
            "source": article.get("source", {}).get("name", "")
        })

    return news_list

print("NEWS_API_KEY:", NEWS_API_KEY)