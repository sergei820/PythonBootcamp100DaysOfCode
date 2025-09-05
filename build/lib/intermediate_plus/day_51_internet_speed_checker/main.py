import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.upload_speed = 0
        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        reject_button = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        reject_button.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        wait_speedtest_passed = WebDriverWait(self.driver, 70)
        wait_speedtest_passed.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Back to test results']")))

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(3)
        self.download_speed = self.driver.find_element(By.CSS_SELECTOR, value='span.download-speed').text
        self.upload_speed = self.driver.find_element(By.CSS_SELECTOR, value='span.upload-speed').text


    def print_compliant_message(self):
        print(f"The internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.print_compliant_message()
    bot.driver.quit()
