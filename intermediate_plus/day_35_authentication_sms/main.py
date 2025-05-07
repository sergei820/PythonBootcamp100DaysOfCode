import os

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ.get("OWM_API_KEY")
LIMASSOL_LATITUDE = 34.707130
LIMASSON_LONGITUDE = 33.022617
CITY_NAME = "Limassol"

# Twilio data
twilio_trial_number = os.environ.get("TWILIO_TRIAL_NUMBER")
twilio_account_sid = os.environ.get("TWILIO_ACC_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_phone = os.environ.get("MY_PHONE")


def check_weather():
    params = {
        "lat": LIMASSOL_LATITUDE,
        "lon": LIMASSON_LONGITUDE,
        "api_key": OWM_API_KEY,
        "appid": OWM_API_KEY,
        "cnt": 8,
    }
    # response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={MY_API_KEY}")
    # print(response.json())

    response = requests.get(OWM_Endpoint, params=params)
    response.raise_for_status()
    timestamps_list = response.json()["list"]
    for three_hr in timestamps_list:
        if three_hr["weather"][0]["id"] < 700:
            print("Bring an umbrella.")
            print(three_hr["weather"][0]["description"])
            return "Rain is expected today, get an umbrella☔️"
    return "Good weather is expected today🌤️"


def send_sms(message_text: str):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        from_=twilio_trial_number,
        messaging_service_sid='MG3f31d40b9a8fa6ea59893981b4b3458f',
        body=message_text,
        to=my_phone
    )
    print(message.status)


if __name__ == "__main__":
    forecast = check_weather()
    # send_sms(forecast)
