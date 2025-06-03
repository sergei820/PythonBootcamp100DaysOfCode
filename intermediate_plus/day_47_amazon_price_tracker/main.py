from os import environ

from bs4 import BeautifulSoup
from requests import get

from intermediate_plus.day_47_amazon_price_tracker.notification_manager import NotificationManager


def start_app():
    notification_manager = NotificationManager()
    my_email = environ.get("ADDR_TO")

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.9",
        "Priority": "u=0, i",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    }

    test_url = "https://appbrewery.github.io/instant_pot/"
    prod_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

    response = get(url=prod_url, headers=headers)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    scraping_result = soup.select_one("div#centerCol span.a-price")  # "div#centerCol span.aok-offscreen"
    # print(soup.prettify())

    print(scraping_result)
    price = scraping_result.getText().replace("$", "").strip()
    print(f"${price}")

    if float(price) < 100.00:
        notification_manager.send_email(my_email, "Price is lower than $100.00")


if __name__ == "__main__":
    start_app()


