from bs4 import BeautifulSoup
# import lxml


with open("website.html", "r") as html_file:
    content = html_file.read()


soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())
