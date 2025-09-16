import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Amazon product URL (replace with your product link)
URL = "https://www.amazon.in/dp/B0C5NN1L9H"  # Example Kindle link

# Headers to pretend like a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.9"
}

# Fetch product page
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract product title and price
title = soup.find(id="productTitle").get_text().strip()
price_str = soup.find("span", class_="a-offscreen").get_text().replace("₹", "").replace(",", "")
price = float(price_str)

print(f"Product: {title}")
print(f"Current Price: ₹{price}")

# Set target price
TARGET_PRICE = 15000.0

# If price drops below target → send email
if price < TARGET_PRICE:
    message = f"Price Alert! The product '{title}' is now at ₹{price}.\nCheck here: {URL}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
    print("✅ Email Sent! Price dropped below target.")
else:
    print("ℹ️ Price is still above target.")
