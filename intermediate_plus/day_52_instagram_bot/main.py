from intermediate_plus.day_52_instagram_bot.InstaFollower import InstaFollower


def start_app():
    insta_follower = InstaFollower()

    insta_follower.login()
    insta_follower.find_followers()
    insta_follower.follow()


if __name__ == "__main__":
    start_app()
