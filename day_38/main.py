import os
import requests
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ---------------- Load environment variables ---------------- #
load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS", "credentials.json")
SHEET_ID = os.getenv("SHEET_ID")

SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPE)
gc = gspread.authorize(credentials)

sheet = gc.open_by_key(SHEET_ID).sheet1  # Always first worksheet

# ---------------- Nutritionix Endpoints ---------------- #
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# ---------------- User Choice ---------------- #
choice = input("Do you want to log (1) Exercise or (2) Food? ")

today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

if choice == "1":
    # ---- Exercise Logging ---- #
    query = input("Tell me what exercises you did: ")
    params = {
        "query": query,
        "gender": "male",
        "weight_kg": 60,
        "height_cm": 168,
        "age": 23
    }
    response = requests.post(exercise_endpoint, json=params, headers=headers)
    result = response.json()

    for exercise in result["exercises"]:
        sheet.append_row([
            today,
            time_now,
            exercise["name"].title(),
            exercise["duration_min"],
            round(exercise["nf_calories"], 2),
            "", "", "", "Exercise"
        ])
    print("✅ Exercise logged to Google Sheet!")

elif choice == "2":
    # ---- Food Logging ---- #
    food_query = input("What did you eat? ")
    food_response = requests.post(nutrition_endpoint, json={"query": food_query}, headers=headers)
    food_result = food_response.json()

    for food in food_result["foods"]:
        sheet.append_row([
            today,
            time_now,
            food["food_name"].title(),
            food["serving_qty"],
            food["nf_calories"],
            f"{food['nf_protein']}g",
            f"{food['nf_total_carbohydrate']}g",
            f"{food['nf_total_fat']}g",
            "Food"
        ])
    print("✅ Food logged to Google Sheet!")

else:
    print("❌ Invalid choice. Please select 1 or 2.")
