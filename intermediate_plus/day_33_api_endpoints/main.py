import requests
from datetime import datetime

LIMASSOL_LATITUDE = 34.707130
LIMASSON_LONGITUDE = 33.022617


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)

    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]
    iss_position = (longitude, latitude)
    print(iss_position)


def get_sunset_times():
    parameters = {
        "lat": LIMASSOL_LATITUDE,
        "lng": LIMASSON_LONGITUDE,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # https://api.sunrise-sunset.org/json?lat=34.707130&lng=33.022617

    response.raise_for_status()
    data = response.json()
    print(data)

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    # To get hours from the full date:
    print(f"sunrise: {sunrise.split("T")[1].split(":")[0]}")


    time_now = datetime.now()
    print(f"time_now: {time_now}")


if __name__ == "__main__":
    # get_iss_position()
    get_sunset_times()
