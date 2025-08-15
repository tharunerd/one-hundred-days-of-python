

# 🎤 Kanye West Quote Generator

A fun little Python project that fetches and displays **Kanye West quotes** from the [kanye.rest](https://kanye.rest/) API.  
Every time you click on Kanye's face, you get a new piece of Kanye wisdom.  

---

## 🚀 Features

- 🖼️ **Interactive GUI** built with `tkinter`
- 🔄 **Random quotes** fetched from the Kanye REST API
- 🖱️ **Click Kanye’s picture** to instantly get a fresh quote
- 🎨 **Custom graphics** for a fun user experience


## 🛠️ Tech Stack

- **Python 3**
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) — GUI toolkit
- [`requests`](https://pypi.org/project/requests/) — For fetching API data
- [Kanye REST API](https://kanye.rest/) — Random Kanye West quotes

---

## 📂 Project Structure

```

📁 kanye-quote-generator
┣ 📜 main.py              # Main application file
┣ 🖼️ background.png       # Background image
┣ 🖼️ kanye.png            # Kanye clickable image
┗ 📜 README.md            # Project documentation

````

---

## ▶️ How to Run

1. **Clone the repository**:
   
2. **Install dependencies**:

   ```bash
   pip install requests
   ```

3. **Run the app**:

   ```bash
   python main.py
   ```

4. **Click Kanye’s face** and enjoy a new quote every time 🎤.

---

## ⚙️ How It Works

1. The app uses the [`requests`](https://pypi.org/project/requests/) library to fetch JSON data from the [Kanye REST API](https://kanye.rest/).
2. The `"quote"` field from the JSON response is extracted.
3. The `tkinter` canvas updates the displayed text with the new quote.
4. Each click of the Kanye image triggers a new API request.

---

## 💡 Ideas for Improvements

* 📌 Add a **"Save Favorite Quote"** feature
* 🌐 Add **offline mode** with locally stored quotes
* 🎵 Play a **sound effect** when generating quotes
* 📱 Make it responsive for different window sizes
