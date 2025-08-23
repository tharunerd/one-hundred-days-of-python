import requests
from datetime import datetime
import os

# Load secrets from environment variables
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

exercise_text = input("Tell me what exercise you did: ")

# Nutritionix API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 168,
    "age": 23
}

response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
print(result)

# Parse and send to Google Sheets via Sheety
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
    print(sheet_response.text)
