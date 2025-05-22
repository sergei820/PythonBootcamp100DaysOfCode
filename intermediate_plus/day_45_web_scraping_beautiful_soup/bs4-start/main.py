from bs4 import BeautifulSoup
# import lxml


with open("website.html", "r") as html_file:
    content = html_file.read()


soup = BeautifulSoup(content, "html.parser")

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# print(soup.prettify())  # returns the whole html

heading = soup(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))
print(soup.find_all("a"))