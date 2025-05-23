import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

def start_app():
    # h3.title
    response = requests.get(url=URL)

    yc_webpage = response.text
    soup = BeautifulSoup(yc_webpage, "html.parser")

    movies = soup.find_all(name="h3", class_="title")

    with open("./movies.txt", "w") as file:
        for movie in movies[::-1]:
            file.write(f"{movie.getText()}\n")


if __name__ == "__main__":
    start_app()

