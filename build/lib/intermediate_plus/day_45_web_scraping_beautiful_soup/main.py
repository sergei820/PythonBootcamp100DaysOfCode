from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

def start_app():
    response = requests.get(url=url)

    yc_webpage = response.text
    soup = BeautifulSoup(yc_webpage, "html.parser")
    # print(soup.prettify())

    # print(soup.find_all(name="a", class="storylink"))

    articles = soup.find_all(name="span", class_="titleline")


    article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

    article_texts = []
    article_links = []

    for article in articles:
        article_text = article.getText()
        article_texts.append(article_text)
        article_link = article.find(name="a").get("href")
        article_links.append(article_link)

    # print(article_texts)
    # print(article_links)
    # print(article_upvotes)

    print(max(article_upvotes))
    index = article_upvotes.index(max(article_upvotes))
    print(article_texts[index])
    print(article_links[index])
    print(article_upvotes[index])


    # for article in articles:
    #     article_text = article.getText()
    #     article_link =
    #     article_upvote =
        # print(article.getText())



if __name__ == "__main__":
    start_app()
