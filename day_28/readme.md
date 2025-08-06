# Day 28 – Pomodoro App ⏲️

## 📌 Overview
On Day 28 of my [#100DaysOfPython](https://github.com/Akula-tharun-kumar/100-Days-of-Python) challenge, I built a **Pomodoro Timer App** using the `tkinter` GUI library in Python.

The **Pomodoro Technique** is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This app helps boost productivity by structuring focused work sessions followed by rest periods.

---

## 🧠 Key Concepts Covered

- GUI Programming using `tkinter`
- Timer mechanisms using `after()` method
- Countdown logic and loop recursion
- Working with global variables
- UI updates and control flow logic
- Use of emojis and Unicode for visual appeal
- Resetting the timer and managing work/break sessions

---

## 📋 Features

✅ 25-minute **work sessions**  
✅ 5-minute **short breaks**  
✅ 20-minute **long break** after 4 work sessions  
✅ Start and Reset buttons  
✅ Visual check marks (✓) for completed sessions  
✅ Minimal and user-friendly UI

---

## 🔧 How It Works

1. Click **Start** to begin the first Pomodoro (work session).
2. After 25 minutes, the app automatically transitions into a **short break**.
3. After four Pomodoros, it switches to a **long break**.
4. Each completed Pomodoro adds a ✔ to track your productivity.
5. You can hit **Reset** any time to start over.

---

## 🗂️ File Structure
```
Day-28/
│
├── main.py # Main file containing GUI and timer logic
├── pomodoro.png # (Optional) Icon/image used in UI
└── README.md # Project documentation
```
---

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Clone this repository or download the `Day-28` folder.
3. Run the following command in your terminal:
   ```bash
   python main.py
   ```
🧰 Tools & Libraries
- Python 3.x
- tkinter – Built-in Python GUI module
- Unicode for emoji symbols

**🧩 What I Learned**

- Creating and managing GUIs using tkinter
- Managing app state using global variables
- Implementing countdowns and timed callbacks in Python
- Structuring real-world productivity tools

