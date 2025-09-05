from os import environ

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()

linkedin_login = environ.get("LINKEDIN_LOGIN")
linkedin_password = environ.get("LINKEDIN_PASSOWRD")

def start_app():
    url = "https://www.linkedin.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(1)

    sign_in_button = driver.find_element(By.CSS_SELECTOR, "nav a.nav__button-secondary")
    sign_in_button.click()

    username_input = driver.find_element(By.CSS_SELECTOR, "input#username")
    password_input = driver.find_element(By.CSS_SELECTOR, "input#password")
    username_input.send_keys(linkedin_login)
    password_input.send_keys(linkedin_password, Keys.ENTER)

    jobs_button = driver.find_element(By.XPATH, "//a[@href='https://www.linkedin.com/jobs/?']")
    jobs_button.click()

    show_all_button = driver.find_element(By.CSS_SELECTOR, ".discovery-templates-vertical-list__footer span")
    show_all_button.click()

    job_cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__entity-lockup")

    for job_card in job_cards:
        job_card.click()
        save_job_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button__text")
        save_job_button.click()


if __name__ == "__main__":
    start_app()
