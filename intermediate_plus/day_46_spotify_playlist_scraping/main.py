from intermediate_plus.day_46_spotify_playlist_scraping.songs_collector import SongsCollector
from intermediate_plus.day_46_spotify_playlist_scraping.spotify_manager import SpotifyManager


def start_app():
    user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")  # "2000-08-12"
    songs_collector = SongsCollector(user_date)
    spotify_manager = SpotifyManager()

    song_names_list = songs_collector.gather_song_names_list()

    songs_year = user_date.split("-")[0]
    spotify_songs_links = spotify_manager.find_songs_links_in_spotify(song_names_list, songs_year)

    playlist_name = f"{user_date} Top Rated"
    playlist_description = f"Top songs from {user_date} based on Billboard."
    spotify_manager.create_spotify_playlist(playlist_name, playlist_description, spotify_songs_links)


if __name__ == "__main__":
    start_app()