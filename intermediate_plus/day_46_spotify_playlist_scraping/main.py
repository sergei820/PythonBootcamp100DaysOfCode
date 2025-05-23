import requests
from bs4 import BeautifulSoup




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


if __name__ == "__main__":
    start_app()