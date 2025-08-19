
---

# 🌍 Day 33 – ISS Locator Email Project

This project is part of my **100 Days of Python Challenge**.
It automatically tracks the **International Space Station (ISS)** and sends an **email alert** when the ISS is visible in your location at night! 🚀✨

---

## 📖 Project Overview

* Uses **Open Notify API** to fetch real-time ISS location.
* Checks if the ISS is near your location (based on latitude & longitude).
* Verifies if it’s **nighttime** at your location using the **Sunrise-Sunset API**.
* If conditions are met → sends you an **email notification** 📧.

---

## ⚙️ Features

✅ Real-time ISS location tracking
✅ Day/Night verification
✅ Automated Email Notifications
✅ Hands-on practice with **APIs, requests, and smtplib**

---

## 🛠️ Tech Stack

* **Python** (requests, smtplib, datetime, time)
* **APIs Used**:

  * [Open Notify ISS API](http://api.open-notify.org/)
  * [Sunrise-Sunset API](https://sunrise-sunset.org/api)
* **SMTP (Email Service)**

---

## 📂 How It Works

1. Script fetches **current ISS position** from API.
2. Compares ISS coordinates with your location.
3. Checks whether the **sun has set** (nighttime check).
4. If ISS is overhead **and** it’s dark → an **email alert is triggered**.

---

## 🚀 Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/tharunerd/100_days_python_course.git
   cd day_33
   ```
2. Update your location (latitude & longitude) inside the script.
3. Add your email credentials (use environment variables for safety).
4. Run the script:

   ```bash
   python main.py
   ```

---

## 📧 Example Alert Email

> Subject: **Look Up! 👀 The ISS is above you!**
> Body: Go outside and watch the sky, the ISS is currently passing by! 🚀✨

---

## 📌 Learning Outcome

This project gave me a deeper understanding of:

* **Working with APIs** (GET requests & JSON data)
* **Automating email alerts with SMTP**
* **Combining multiple services for a real-world utility**

---

