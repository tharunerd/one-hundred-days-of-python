from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib3
import os
from dotenv import load_dotenv

# -------- Suppress SSL warnings --------
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# -------- Load environment variables --------
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# -------- Scraping Billboard 100 --------
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=billboard_url, headers=header, verify=False)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# -------- Spotify Authentication --------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(f"✅ Logged in as: {user_id}")

# -------- Searching Spotify for songs --------
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"⚠️ {song} not found on Spotify. Skipping...")

# -------- Creating new private playlist --------
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 songs from Billboard Hot 100 on {date}"
)
print(f"🎶 Created Playlist: {playlist['name']}")

# -------- Adding songs to playlist --------
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"✅ Added {len(song_uris)} songs to {playlist['name']}")
