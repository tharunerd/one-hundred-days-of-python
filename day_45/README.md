
# 🎬 Day 45: 100 Movies That You Must Watch  

## 📖 Overview
On **Day 45** of Angela Yu’s *100 Days of Python* course, I built a **Web Scraping project** using **BeautifulSoup**.  

The goal was simple but exciting:  
👉 Scrape the **Top 100 Movies of All Time** from Empire’s website (via Internet Archive) and save them into a `movies.txt` file.  

This project introduced me to the **power of web scraping**, working with HTML data, and automating information extraction.  

---

## 🎯 Objective
- Scrape the top **100 movie titles** from a web page.  
- Store them neatly in a text file (`movies.txt`).  
- Ensure the movies are listed in **ascending order** (starting from 1).  

Example output:
```

1. The Godfather
2. The Empire Strikes Back
3. The Dark Knight
4. The Shawshank Redemption
   ... and so on

```

---

## ⚙️ Technologies Used
- **Python 3.x**  
- **BeautifulSoup4** → parsing HTML content  
- **Requests** → making HTTP requests  
- **Internet Archive (Wayback Machine)** → stable webpage source  

---

## 🌐 Data Source
Since websites change frequently, this project uses the **archived version** of Empire’s Top 100 Movies page:  


[https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/)



---

## 📂 Project Structure
```

day\_45\_100\_movies/
│
├── main.py        # Python script for scraping
├── movies.txt     # Final output file with 100 movies
└── README.md      # Project documentation

````

---

## 🚀 How to Run
1. Clone the repository:
   ```
   https://github.com/tharunerd/one-hundred-days-of-python.git
   cd day_45
   ```

2. Install the required dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the script:

   ```bash
   python main.py
   ```

4. Open `movies.txt` to see the full list 🎉

---

## 🧠 Key Learnings

* Using **BeautifulSoup** to parse HTML.
* Extracting and cleaning **real-world data** from websites.
* Writing results to a file in a clean format.
* Understanding the importance of **archived web pages** for consistent scraping.

---

## 🔮 Future Improvements

* Save results in **CSV or JSON** format for easy data handling.
* Build a **Flask/Django web app** to display the movies interactively.
* Add functionality to scrape **other movie lists** (IMDb, Rotten Tomatoes).

---

💡 *This project showed me how easy and powerful it is to collect data from the web. With just a few lines of Python, I can automate data gathering and create my own datasets.*


