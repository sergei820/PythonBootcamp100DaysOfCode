import requests
from bs4 import BeautifulSoup
from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

spotify_client_id = environ.get("SPOTIFY_CLIENT_ID")
spotify_client_secret = environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = "http://127.0.0.1:8888/callback"


def start_app():
    user_date = "2000-08-12"  #  input("Which year do you want tot travel to? Type the date in this format YYYY-MM-DD:")
    billboard_url = f"https://www.billboard.com/charts/hot-100/{user_date}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Version/18.4 Safari/605.1.15"
        )
    }
    response = requests.get(url=billboard_url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select("li > ul > li > h3")

    for song in results:
        print(song.getText().strip())

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-modify-private"
    ))

    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name="My Private Playlist", public=False)

    print("Created playlist:", playlist["name"])


if __name__ == "__main__":
    start_app()