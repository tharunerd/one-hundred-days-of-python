
---

# 📈 Day 36 - Stock Trading News Alert

This project is part of the **100 Days of Python** course.
It sends you **stock market updates** with related **news articles** directly to your phone via **SMS** using Twilio.

---

## 🚀 How It Works

1. Fetches **stock price data** using [Alpha Vantage API](https://www.alphavantage.co/).
2. Checks if the stock price has a **significant change (5% or more)**.
3. If yes → fetches **latest company news** from [NewsAPI](https://newsapi.org/).
4. Sends an **SMS alert** with stock price movement + top 3 news headlines.

---

## 🛠 Requirements

* Python 3.8+
* Twilio account (for sending SMS)
* Alpha Vantage API key (for stock data)
* News API key (for news articles)

Install dependencies:

```bash
pip install requests twilio
```

---

## 🔑 API Keys & Config

In your `main.py`, replace these placeholders with your actual keys:

```python
NEWS_API_KEY = "your_news_api_key"
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
ACCOUNT_SID = "your_twilio_account_sid"
AUTH_TOKEN = "your_twilio_auth_token"
FROM_NUMBER = "your_twilio_phone_number"
TO_NUMBERS = ["+91XXXXXXXXXX", "+91YYYYYYYYYY"]  # Multiple receivers supported
```

👉 `TO_NUMBERS` is now a list. Add multiple numbers inside the list.

---

## ▶️ How to Run

```bash
python main.py
```

If there’s a significant stock price change, you’ll receive an SMS like:

```
TSLA: 🔻-5.6% 
Headline: Tesla faces supply chain delays 
Brief: The company announced new delivery targets amid chip shortages...
```

---

## 📂 Project Structure

```
Day36_StockNewsAlert/
│── main.py
│── README.md
│── .env
│── .gitignore
│── .project_config

```

---

## 📸 Demo SMS

Example SMS received on phone:

```
TSLA: 🔺+6.2%
Headline: Tesla releases new model in India
Brief: The electric carmaker launched its Model Y with huge preorders...
```

---

## 🌟 Why This Project is Useful

* Automates **stock monitoring**.
* Gives you **instant news alerts**.
* Can be extended for **multiple companies**.
* Shows power of **APIs + Automation** with Python.

---
