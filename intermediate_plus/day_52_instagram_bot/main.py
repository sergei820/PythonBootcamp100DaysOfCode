from intermediate_plus.day_52_instagram_bot.InstaFollower import InstaFollower
from selenium import webdriver

def start_app():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    insta_follower = InstaFollower(driver)

    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()

    driver.quit()


if __name__ == "__main__":
    start_app()
