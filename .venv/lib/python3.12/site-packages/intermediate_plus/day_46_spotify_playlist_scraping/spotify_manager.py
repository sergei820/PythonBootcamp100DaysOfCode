from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


class SpotifyManager:
    def __init__(self):
        self.spotify_client_id = environ.get("SPOTIFY_CLIENT_ID")
        self.spotify_client_secret = environ.get("SPOTIFY_CLIENT_SECRET")
        self.redirect_uri = "http://127.0.0.1:8888/callback"
        self.spotify_api_client = self.sp_auth()
        self.user_id = self.spotify_api_client.current_user()["id"]

    def sp_auth(self):
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.spotify_client_id,
            client_secret=self.spotify_client_secret,
            redirect_uri=self.redirect_uri,
            scope="playlist-modify-private"
        ))

    def find_songs_links_in_spotify(self, track_names_list: list, track_year: str) -> list:
        print(f"Spotify user ID is: {self.user_id}")

        spotify_track_links = []

        for song in track_names_list:
            try:
                query = f"track:{song} year:{track_year}"
                result = self.spotify_api_client.search(q=query, type="track", limit=1)
                tracks = result["tracks"]["items"]
                if tracks:
                    uri = tracks[0]["uri"]
                    spotify_track_links.append(uri)
                else:
                    print(f"Song '{song}' not found")
            except Exception as e:
                print(f"Song '{song}' not found: {e}")

        print(f"\nFound {len(spotify_track_links)} songs.")

        return spotify_track_links


    def create_spotify_playlist(self, playlist_name: str, playlist_description: str, spotify_songs_links: list) -> None:
        playlist = self.spotify_api_client.user_playlist_create(
            user=self.user_id,
            name=playlist_name,
            public=False,
            description=playlist_description
        )

        playlist_id = playlist["id"]
        print(f"Created playlist: {playlist_name} (ID: {playlist_id})")

        self.spotify_api_client.playlist_add_items(playlist_id=playlist_id, items=spotify_songs_links)
        print("Added all tracks to playlist!")
