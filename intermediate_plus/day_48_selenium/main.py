from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def init_driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    return driver


def start_app():
    test_url = "https://appbrewery.github.io/instant_pot/"

    driver = init_driver()
    # driver.get("https://www.amazon.com")

    driver.get(test_url)

    prie_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    print(f"The price is ${prie_dollar.text}.{price_cents.text}")

    driver.quit()


def run_challenge_1():
    url = "https://www.python.org/"
    driver = init_driver()

    driver.get(url)
    driver.implicitly_wait(1)

    event_time_path = ".event-widget li time"
    event_link_path = ".event-widget li a"
    time_list = driver.find_elements(By.CSS_SELECTOR, value=event_time_path)
    events_list = driver.find_elements(By.CSS_SELECTOR, value=event_link_path)

    events_dict = {}

    for i in range(len(events_list)):
        events_dict[i] = {'time': time_list[i].text, 'name': events_list[i].text}

    print(events_dict)


def run_challenge_2():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    driver = init_driver()
    driver.get(url)

    articlecount = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")[1].text
    print(articlecount)


def practice_buttons_clicking():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    driver = init_driver()
    driver.get(url)

    search_input = driver.find_element(By.NAME, value="search")
    search_input.send_keys("Python", Keys.ENTER)


def run_challenge_3():
    url = "http://secure-retreat-92358.herokuapp.com"
    driver = init_driver()
    driver.get(url)

    fName = driver.find_element(By.NAME, value="fName")
    lName = driver.find_element(By.NAME, value="lName")
    email = driver.find_element(By.NAME, value="email")

    fName.send_keys("123")
    lName.send_keys("321")
    email.send_keys("qwe@rty.com", Keys.ENTER)

    success_form = driver.find_element(By.CSS_SELECTOR, value=".display-3")

    print(success_form.text)


if __name__ == "__main__":
    # start_app()
    # run_challenge_1()
    # run_challenge_2()
    # practice_buttons_clicking()
    run_challenge_3()
