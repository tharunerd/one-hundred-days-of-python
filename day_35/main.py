import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------------------- #
#   CONFIGURATION
# ------------------------------- #
OWM_Endpoint = os.getenv("OWM_ENDPOINT")
API_KEY = os.getenv("API_KEY")

# Your latitude & longitude (example: gurgaon, India)
MY_LAT = 28.4595
MY_LON = 77.0266


# Twilio details
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")

# Get and split phone numbers
to_numbers_raw = os.getenv("TO_NUMBERS")
if not to_numbers_raw:
    raise ValueError("TO_NUMBERS is not set in the .env file.")
TO_NUMBERS = [num.strip() for num in to_numbers_raw.split(",")]

# ------------------------------- #
#   FETCH WEATHER DATA
# ------------------------------- #
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,  # next 4 time slots (~12 hours)
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# ------------------------------- #
#   CHECK FOR RAIN
# ------------------------------- #
will_rain = False

for forecast in weather_data["list"]:
    condition_code = forecast["weather"][0]["id"]
    if int(condition_code) < 700:  # codes < 700 mean rain/snow
        will_rain = True
        break

# ------------------------------- #
#   SEND SMS ALERT
# ------------------------------- #
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for number in TO_NUMBERS:
        message = client.messages.create(
            body="🌧 It's going to rain today! Remember to bring an umbrella ☂️",
            from_=FROM_NUMBER,
            to=number,
        )
        print(f"Sent to {number}: SID={message.sid}, Status={message.status}")
else:
    print("No rain expected today. You're good to go!")
