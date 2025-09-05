import requests
from bs4 import BeautifulSoup


class SongsCollector:
    def __init__(self, date: str):
        self.billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

    def gather_song_names_list(self) -> list:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                "(KHTML, like Gecko) Version/18.4 Safari/605.1.15"
            )
        }
        response = requests.get(url=self.billboard_url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        scraping_result = soup.select("li > ul > li > h3")

        songs_list = [song.getText().strip() for song in scraping_result]

        return songs_list
