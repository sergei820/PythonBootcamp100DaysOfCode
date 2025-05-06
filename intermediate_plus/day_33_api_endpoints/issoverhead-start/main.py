import requests
from datetime import datetime
import time

import smtplib
import os
from dotenv import load_dotenv


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")
ADDR_TO = os.getenv("ADDR_TO")

mail_host = "smtp.gmail.com"
mail_port = 587

load_dotenv()

LIMASSOL_LATITUDE = 34.707130
LIMASSON_LONGITUDE = 33.022617

def start_app():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": LIMASSOL_LATITUDE,
        "lng": LIMASSON_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"sunset: {sunset}")

    def send_email(to_addrs: str, message: str):
        with smtplib.SMTP(mail_host, port=mail_port) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=to_addrs,
                msg=message
            )

    #If the ISS is close to my current position
    def is_not_far(lat: float, lng: float) -> bool:
        is_lat_not_far = abs(lat - LIMASSOL_LATITUDE) <= 5
        is_lng_not_far = abs(lng - LIMASSON_LONGITUDE) <= 5
        return is_lat_not_far and is_lng_not_far

    # and it is currently dark
    def is_it_dark(sunrise: int, sunset: int) -> bool:
        time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])
        print(f"time_now: {time_now}")
        return sunrise > time_now > sunset


    print(is_it_dark(sunrise, sunset))

    # Then send me an email to tell me to look up.
    def send_email_iss_is_visible(lat, lng, email):
        if is_not_far(lat, lng) and is_it_dark(sunrise, sunset):
            send_email(email, "Look up!")
    # BONUS: run the code every 60 seconds.

    while True:
        time.sleep(60)
        send_email_iss_is_visible(iss_latitude, iss_longitude, ADDR_TO)


if __name__ == "__main__":
    start_app()
