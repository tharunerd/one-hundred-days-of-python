import requests
from datetime import datetime, timezone
import smtplib
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive info from environment variables
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587 if not set

# Your location (latitude & longitude)
MY_LAT = 51.507351
MY_LONG = -0.127758

# ---------------------- Function: Check if ISS is Overhead ---------------------- #
def is_iss_overhead():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_lat = float(data["iss_position"]["latitude"])
        iss_long = float(data["iss_position"]["longitude"])

        return (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LONG - 5 <= iss_long <= MY_LONG + 5)
    except Exception as e:
        print(f"Error checking ISS position: {e}")
        return False

# ---------------------- Function: Check if it's Night ---------------------- #
def is_night():
    try:
        params = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=params)
        response.raise_for_status()
        data = response.json()

        sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        current_hour = datetime.now(timezone.utc).hour

        return current_hour >= sunset_hour or current_hour <= sunrise_hour
    except Exception as e:
        print(f"Error checking day/night status: {e}")
        return False

# ---------------------- Function: Send Email ---------------------- #
def send_email():
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# ---------------------- Main Loop ---------------------- #
def main():
    print("Starting ISS overhead notifier...")
    while True:
        time.sleep(60)
        if is_iss_overhead() and is_night():
            send_email()

if __name__ == "__main__":
    main()
