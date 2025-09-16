# 🚀 100 Days of Python – Day 46

## 🎶 Billboard 100 → Spotify Playlist Generator

### 📅 Day 46 Progress

On **Day 46**, I worked on connecting **web scraping skills** with **API integration**.
This project combines everything I’ve learned so far into something exciting and real-world:

* Scraping live data from a website (Billboard Hot 100).
* Working with authentication flows (Spotify OAuth).
* Using a third-party API (Spotify Web API).
* Automating playlist creation.

Every day, my projects get one step closer to solving **real problems** while making my GitHub portfolio shine ✨.

---

## 🎯 Project Goal

Create a program that:

1. Scrapes the **Billboard Hot 100 songs** for a user-given date.
2. Searches those songs on **Spotify**.
3. Creates a **private playlist** in the user’s account.
4. Adds all available songs into the playlist automatically.

It’s like **time-traveling through music** — you can revisit the top songs from any day in history. 🎵

---

## 🛠️ Tools & Libraries Learned Today

* **BeautifulSoup4** → Scraping Billboard’s Hot 100 chart.
* **Requests** → Fetching webpage content.
* **Spotipy** → Python client for Spotify API.
* **SpotifyOAuth** → Handling login and secure access tokens.

---

## ⚙️ How the Code Works

1. **User Input**

   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
   ```

   Example: `2002-07-15`

2. **Billboard Scraping**

   * Extract top 100 songs from Billboard Hot 100 page.

3. **Spotify Authentication**

   * Log into Spotify using OAuth.
   * Get current user ID.

4. **Song Search & Playlist Creation**

   * Search for each Billboard song in Spotify.
   * Skip missing ones.
   * Create playlist named:

     ```
     YYYY-MM-DD Billboard 100
     ```
   * Add all found songs into it.

---

## 📸 Example Run

✅ Input: `2010-05-20`
➡️ Creates a playlist called **“2010-05-20 Billboard 100”** in Spotify with the top songs of that week.

---

## 🌟 What I Learned on Day 46

* How to combine **web scraping + API calls**.
* Handling missing data (not every Billboard song exists on Spotify).
* Automating playlist creation with **user authentication**.
* End-to-end integration: scrape → process → API → automation.

---

## 🔮 Next Steps 

* Expand scraping to **Top 200 Global / Regional charts**.
* Add GUI (date picker) for a better user experience.
* Option to share playlists publicly.
