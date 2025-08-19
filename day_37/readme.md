# 🌱 Day 37 – Habit Tracker

This project is a **Habit Tracker** built using **Python** and the **Pixela API**, where you can create, track, and visualize your daily habits in the form of a graph 📊. It’s a great way to stay consistent and accountable in building positive routines! 

ANd all the actions relate dto API like creation, updation, deleting and logging happened via CLI(aommand line interface)

---

## 🚀 Features

* 📌 **Create a new user** on Pixela 
* 🟢 **Create a graph** for tracking habits (exercise, coding, reading, etc.)
* ➕ **Add daily progress (pixels)** to track habits visually
* ✏️ **Update entries** if you make changes
* ❌ **Delete entries** when needed
* 🖼️ **Graph visualization** for motivation

---

## 🛠️ Technologies Used

* **Python 3** 🐍
* **Requests Library** for API communication
* **Pixela API** ([https://pixe.la](https://pixe.la)) for habit tracking and visualization

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tharunerd/100_days_python_course.git

cd day_37
```

### 2. Install Dependencies

```bash
pip install requests python-dotenv
```

### 3. Add Environment Variables

Create a `.env` file in the `day_37` folder and add:

```env
PIXELA_USERNAME=your_pixela_username
PIXELA_TOKEN=your_pixela_token
GRAPH_ID=habitgraph
```

*(Use a strong token, recommended at least 8 characters with letters & numbers)*

### 4. Run the Script

```bash
python main.py
```

---

## 📊 Example Output

* Create graph: `https://pixe.la/v1/users/<tharun>/graphs/habitgraph`
* Each day you add progress, you’ll see a pixel on the graph:

![Habit Tracker Example](https://user-images.githubusercontent.com/yourusername/habit-tracker-demo.png)

---

## 💡 What I Learned

* How to use **REST APIs** in Python
* Handling **POST, PUT, and DELETE requests**
* Working with **environment variables** for security
* Visualizing data using external services

---

## ✅ Use Cases

* Track **exercise** 🏋️
* Build a **coding streak** 💻
* Daily **reading tracker** 📚
* Any personal habit you want to stay consistent with!

---
