# Day 34: Quiz App – 100 Days of Python

A **Graphical Quiz App** built using **Python** and **Tkinter** as part of Angela Yu's 100 Days of Python course.
This app allows users to answer multiple-choice questions and see their score in real-time with visual feedback.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [How It Works](#how-it-works)
6. [How to Run](#how-to-run)
7. [Key Learning Points](#key-learning-points)
8. [Future Improvements](#future-improvements)

---

## Overview

On **Day 34** of Angela Yu's course, we created a **Quiz App** that demonstrates:

* **GUI programming** with Tkinter
* Interactive quizzes with **True/False questions**
* Real-time **score tracking** and visual feedback

The app is beginner-friendly and easy to extend with more questions or different categories.

---

## Features

* Clean **GUI interface** built with Tkinter
* Interactive **True/False quiz questions**
* Real-time **score tracking**
* Visual feedback using **images** (`true.png` / `false.png`)
* Easily extendable with more questions

---

## Technologies Used

* **Python 3.x**
* **Tkinter** for GUI
* **Object-Oriented Programming (OOP)** for quiz logic

---

## Project Structure

```
quiz-app/
│
├── data.py               # Stores quiz questions (from API or local data)
├── question_model.py     # Defines the Question class
├── quiz_brain.py         # Handles quiz logic, scoring, and question flow
├── ui.py                 # Builds the GUI interface
├── main.py               # Launches the Quiz App
└── images/               # Feedback images
    ├── true.png
    └── false.png
```

---

## How It Works

1. **data.py** – Stores a list of questions and answers.
2. **question\_model.py** – Defines the **Question class** for structured question objects.
3. **quiz\_brain.py** –

   * Keeps track of the current question
   * Checks user answers
   * Updates the score
4. **ui.py** –

   * Displays questions and options in a GUI
   * Handles button clicks from the user
   * Shows **visual feedback** using images
5. **main.py** – Launches the app and connects the GUI with quiz logic

---

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/tharunerd/one-hundred-days-of-python.git
```

2. **Navigate into the project folder:**

```bash
cd day_34
```

3. **Run the app:**

```bash
python main.py
```

> After completing the quiz, your final score will be displayed both in the GUI and in the terminal.

---

## Key Learning Points

* Building a GUI with **Tkinter**
* Using **images** for interactive feedback
* Structuring code with **OOP** principles
* Managing application state (**current question, score**)
* Dynamically updating the GUI based on user input

---

## Future Improvements

* Add a **timer** for each question
* Store **high scores** locally
* Add **categories or difficulty levels**
* Enhance the GUI with **colors, fonts, animations, and sound effects**

---
