import smtplib
import os
from dotenv import load_dotenv
from random import randint

import datetime as dt

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")
ADDR_TO = os.getenv("ADDR_TO")

mail_host = "smtp.gmail.com"
mail_port = 587

def send_email(to_addrs: str, message: str):
    with smtplib.SMTP(mail_host, port=mail_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_addrs,
            msg=message
        )


def start_app():
    # get a weekday
    now = dt.datetime.now()
    # print(now.weekday())  # 0 -> Monday

    # get a message from a file
    quotes = []
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    motivational_quote = quotes[randint(0, len(quotes)-1)]
    print(motivational_quote)

    # send an email
    if now.weekday() == 0:  # 0 -> Monday
        send_email(ADDR_TO, f"Subject:Motivational quote\n\n{motivational_quote}")



if __name__ == "__main__":
    start_app()
