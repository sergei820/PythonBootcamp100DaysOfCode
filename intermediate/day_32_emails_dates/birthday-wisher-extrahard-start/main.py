import datetime as dt
import csv
import smtplib
import os
from dotenv import load_dotenv
from random import randint


load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")
ADDR_TO = os.getenv("ADDR_TO")

mail_host = "smtp.gmail.com"
mail_port = 587


##################### Extra Hard Starting Project ######################
def start_app():
    today_day = dt.datetime.now().day
    today_month = dt.datetime.now().month

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    def prepare_message(recipient_name: str) -> str:
        with open(f"letter_templates/letter_{randint(1,3)}.txt", "r") as letter_file:
            letter = letter_file.read()
            print(letter)
            return letter.replace("[NAME]", recipient_name)

    # 4. Send the letter generated in step 3 to that person's email address.
    def send_email(to_addrs: str, message: str):
        with smtplib.SMTP(mail_host, port=mail_port) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=to_addrs,
                msg=message
            )

    # 1. Update the birthdays.csv
    with open("birthdays.csv", "a") as file:
        file.write(f"\nPerson_with_birthday_today,{ADDR_TO},1991,{today_month},{today_day}")

    # 2. Check if today matches a birthday in the birthdays.csv
    with open("birthdays.csv", "r") as birthdays_file:
        reader = csv.DictReader(birthdays_file)
        for row in reader:
            if int(row["day"]) == today_day and int(row["month"]) == today_month:
                send_email(row["email"],prepare_message(row["name"]))


if __name__ == "__main__":
    start_app()
