
# 📦 Day 47 – Amazon Price Tracker

## 🚀 Objective
Build a Python script that tracks the price of an Amazon product and sends you an email notification when the price drops below your desired target.

## 🔧 Features
- Scrapes product **title** and **price** from Amazon.
- Compares price to your **target budget**.
- Sends an **email alert** when the price drops.
- Uses **environment variables (.env)** to keep credentials safe.

---

## 📂 Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/tharunerd/100-days-python-course.git
cd day_47
````

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 python-dotenv
```

### 3. Create a `.env` file

```ini
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password
TO_EMAIL=recipient_email@gmail.com
```

⚠️ For Gmail, create an **App Password** from your Google account.

---

## ▶️ Running the Script

```bash
python main.py
```

* The script fetches the product page.
* Extracts **title** and **price**.
* If price is lower than your target → sends an email notification.

---

## 📸 Example Output

```
Product: Kindle Paperwhite (11th Gen)
Current Price: ₹12999.0
✅ Email Sent! Price dropped below target.
```

---

## 📚 Learnings

* Web scraping with **BeautifulSoup**.
* Automating tasks with **Python & SMTP**.
* Keeping credentials secure with **dotenv**.
* Real-world automation project: **price monitoring**.


