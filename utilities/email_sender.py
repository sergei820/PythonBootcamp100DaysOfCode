import os
import smtplib

from dotenv import load_dotenv

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