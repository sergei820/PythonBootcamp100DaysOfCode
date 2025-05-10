from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

APP_ID = environ.get("NUTRITIONIX_APP_ID")
API_KEY = environ.get("NUTRITIONIX_API_KEY")

domain = "https://trackapi.nutritionix.com/"
endpoint = "v2/natural/exercise"

def start_app():
    user_input = input("Tell me the exercise you did: ")

    headers = {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }
    body = {
        "query": user_input,
    }

    response = requests.post(url=domain+endpoint, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    start_app()
