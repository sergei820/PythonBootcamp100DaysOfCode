import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
from os import environ

from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

target_account = environ.get("TARGET_ACCOUNT")

login = environ.get("INSTAGRAM_USERNAME")
password = environ.get("INSTAGRAM_PASSWORD")

instagram_base_url = "https://www.instagram.com/"
instagram_login_url = instagram_base_url + "accounts/login/"
instagram_target_account = instagram_base_url + target_account



class InstaFollower:
    def __init__(self, driver):
        self.driver = driver
        self.target_followers_follow_buttons = None

    def login(self):
        self.driver.get(instagram_login_url)

        # time.sleep(50)
        decline_cookies_button = self.driver.find_element(By.XPATH, "//button[text()='Decline optional cookies']")
        decline_cookies_button.click()

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.clear()
        username_input.send_keys(login)

        password_input.clear()
        password_input.send_keys(password, Keys.ENTER)

        not_now_button = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        not_now_button.click()


    def find_followers(self):
        self.driver.get(instagram_target_account)
        followers_link = self.driver.find_element(By.XPATH, "//span[contains(text(), 'followers')]")
        followers_link.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='heading']")))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button/div/div[text()='Follow']")))
        self.target_followers_follow_buttons = self.driver.find_elements("//button/div/div[text()='Follow']")

    def follow(self):
        for button in self.target_followers_follow_buttons:
            button.click()
        time.sleep(30)

