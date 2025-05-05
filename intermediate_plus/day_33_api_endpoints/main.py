import requests

def start_app():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)

    longitude = response.json()["iss_position"]["longitude"]
    latitude = response.json()["iss_position"]["latitude"]
    iss_position = (longitude, latitude)
    print(iss_position)


if __name__ == "__main__":
    start_app()
