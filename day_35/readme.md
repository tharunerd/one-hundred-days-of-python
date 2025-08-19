# Day 35 – Rain Alert App,  🌧️

This project is part of the **100 Days of Python Course (Day 35)** by Angela Yu.
The goal of this day is to **learn how APIs work with authentication** (API keys, parameters, and environment variables) while building a small useful project.

---

## 📌 What this project does

* Connects to a **Weather API** (like OpenWeatherMap).
* Checks if it will rain in your city.
* If rain is expected, the app sends you an **SMS alert** using **Twilio API**.

So, instead of checking the weather every day, you get a quick notification like:
*"It’s going to rain today, bring an umbrella!"* ☂️

---

## 🛠️ Tech & Concepts Learned

* **APIs (Application Programming Interfaces)** → How apps talk to each other.
* **API Keys** → Like passwords for using APIs safely.
* **HTTP requests** with `requests` library.
* **Twilio API** → To send SMS.
* **Environment Variables** → To keep API keys safe (not hard-coded).

---

## 📂 Project Structure

```
Day-35-Rain-Alert/
│
├── main.py              # Main Python file
├── .env                 # to store environment variables and sensitive data(API keys and mobile numbers)
├── .gitignore           # to hide .env file     
├── requirements.txt     # Required libraries
└── README.md            # This file
```

---

## ▶️ How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/tharunerd/one-hundred-days-of-python.git

   cd day-35-rain-alert
   ```

2. Install the required Python libraries:

   ```bash
   pip install twilio
   ```

3. Get your **API Keys**:

   * [OpenWeatherMap API](https://openweathermap.org/api) (for weather data)
   * [Twilio API](https://www.twilio.com/) (for SMS)

4. Store them safely (in `.env` file or environment variables):

   ```
    OWM_ENDPOINT=https://api.openweathermap.org/data/2.5/forecast
    API_KEY=your_api_key
    ACCOUNT_SID=your_sid
    AUTH_TOKEN=your_auth_tokens
    FROM_NUMBER=your_twilio_number
    TO_NUMBERS="reveivers_phone_numbers"

   ```

5. Run the app:

   ```bash
   python main.py
   ```

---

## ✅ Example Output

If rain is expected, you’ll get an SMS:

```
It’s going to rain today ☔ Don’t forget your umbrella!
```

If not, no message will be sent.

---

## 📝 Notes for Beginners

* You **must sign up** for the APIs to get free API keys.
* Never share your API keys publicly (treat them like passwords).
* This project is **just for practice**, so you can hard-code keys at first, but later move them to `.env`.

---

