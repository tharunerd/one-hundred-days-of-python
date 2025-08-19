import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBERS = os.getenv("TO_NUMBERS")

# STEP 1: Get stock data
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
}

response = requests.get(stock_url, params=stock_params, verify=False)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / yesterday_closing_price) * 100, 2)

# STEP 2: If stock price change > 5% -> fetch news
if abs(diff_percent) > 5:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3,
    }
    news_response = requests.get(news_url, params=news_params, verify=False)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # STEP 3: Send each article via SMS
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in articles:
        message_body = (
            f"{STOCK}: {up_down}{diff_percent}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}\n"
            f"URL: {article['url']}"
        )

        for number in TO_NUMBERS:  # Send to multiple recipients
            message = client.messages.create(
                body=message_body,
                from_=FROM_NUMBER,
                to=number.strip(),
            )
            print(f"Message sent to {number}: {message.sid}")
