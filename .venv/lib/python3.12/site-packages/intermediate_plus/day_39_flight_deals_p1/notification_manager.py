import os
from email.mime.text import MIMEText

import requests
from datetime import datetime, timedelta
import smtplib

from dotenv import load_dotenv

# SMTP Data
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")
ADDR_TO = os.getenv("ADDR_TO")
mail_host = "smtp.gmail.com"
mail_port = 587

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def send_email(self, to_addrs: str, message: str):
        mime_message = MIMEText(message, _charset="utf-8").as_string()
        with smtplib.SMTP(mail_host, port=mail_port) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=to_addrs,
                msg=mime_message
            )
