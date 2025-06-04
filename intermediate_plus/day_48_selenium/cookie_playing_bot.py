import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def click_element_for_seconds(webelement, seconds: int) -> None:
    for _ in range(seconds):
        for _ in range(10):
            webelement.click()
        time.sleep(1)

def buy_the_most_expensive_item():
    items_path = "#store div"
    items = driver.find_elements(By.CSS_SELECTOR, value=items_path)
    for item in reversed(items):
        if item.get_attribute("class") != "grayed":
            item.click()
            break


def start_app():
    url = "http://orteil.dashnet.org/experiments/cookie/"

    driver.get(url)

    cookie = driver.find_element(By.ID, value="cookie")

    for _ in range(6):
        click_element_for_seconds(webelement=cookie, seconds=5)
        buy_the_most_expensive_item()

    cookies_per_sec = driver.find_element(By.ID, value="cps").text
    print(f"cookies/seconds: {cookies_per_sec}")

    driver.quit()


if __name__ == "__main__":
    start_app()
