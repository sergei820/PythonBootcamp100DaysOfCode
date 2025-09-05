import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("APP_PASSWORD")
        self.ADDR_TO = os.getenv("ADDR_TO")
        self.mail_host = "smtp.gmail.com"
        self.mail_port = 587

    def send_email(self, to_addrs: str, message: str):
        mime_message = MIMEText(message, _charset="utf-8").as_string()
        with smtplib.SMTP(self.mail_host, port=self.mail_port) as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)
            connection.sendmail(
                from_addr=self.EMAIL,
                to_addrs=to_addrs,
                msg=mime_message
            )

    def send_emails(self, emails_list: list, message: str):
        for email in emails_list:
            self.send_email(email, message)
