
# 🏋️ Workout Tracker with Google Sheets & Nutritionix API

**Day 38 Project – 100 Days of Python Bootcamp**

Track your workouts effortlessly using natural language input! This Python-based app uses the Nutritionix API to calculate calories burned and logs your activity directly into a Google Sheet.

---

## 🚀 Features

- 🗣️ **Natural Language Input**  
  Just type something like: `"Ran 3 miles and did 20 pushups"` — the app understands and processes it!

- 🔥 **Calorie Calculation**  
  Automatically fetches calorie data using the Nutritionix API.

- 📊 **Google Sheets Integration**  
  Logs your workout details (exercise, duration, calories, etc.) into a Google Sheet for easy tracking.

---

## 🛠️ Tech Stack

- **Python**
- **Nutritionix API**
- **Google Sheets API**
- `gspread`, `oauth2client`, `requests`

---

## 📦 Installation

### 1. Clone the Repository

### 2. Install Dependencies

```bash
pip install requests gspread oauth2client
```

### 3. Setup Google Sheets API

- Create a project in Google Cloud Console
- Enable the **Google Sheets API**
- Create credentials and download the `credentials.json` file
- Share your Google Sheet with the email in your credentials (usually ends with `@gmail.com`)

### 4. Configure Nutritionix API

- Sign up at Nutritionix
- Get your **App ID** and **API Key**
- Add them to your environment or directly in the script

### 5. Run the App

```bash
python main.py
```

---

## 📁 File Structure

```
workout-tracker/
│
├── main.py               # Main script to run the tracker
├── .env                  # Google Sheets API credentials
├── CREDENTIALS.JSON      # Python dependencies
└── README.md             # Project documentation
```

---

## ✅ Example Output

```text
Enter your workout: Ran 3 miles and did 20 pushups

Logged to Google Sheet:
- Exercise: Running
- Duration: 30 mins
- Calories: 300
- Date: 2025-08-23
```

---

## 🙌 Contributing

Pull requests are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---
