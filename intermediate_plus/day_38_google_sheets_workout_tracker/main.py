from datetime import datetime
from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

APP_ID = environ.get("NUTRITIONIX_APP_ID")
API_KEY = environ.get("NUTRITIONIX_API_KEY")

domain = "https://trackapi.nutritionix.com/"
endpoint = "v2/natural/exercise"

google_doc_id = environ.get("GOOGLE_DOC_ID")
page_name = "page1"
sheety_endpoint = f"https://api.sheety.co/{google_doc_id}/workoutTracking/{page_name}"
sheety_bearer_auth_token = environ.get("SHEETY_BEARER_AUTH_TOKEN")

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

    # Date	        Time	    Exercise	Duration	Calories
    # 21/07/2020	15:00:00	Running	    22	        130

    def write_to_google_docs(data: dict) -> None:
        sheety_header = {
            "Authorization": sheety_bearer_auth_token,
        }
        sheety_body = {
            "page1": data,
        }
        sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_header)
        print(sheety_response.status_code)

    today = datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")

    for exercise in response.json()["exercises"]:
        exercise_name = exercise["name"]
        duration = response.json()["exercises"][0]["duration_min"]
        calories = response.json()["exercises"][0]["nf_calories"]

        print(f"{date} {time} {exercise} {duration} {calories}")
        exercise_data = {
                "date": date,
                "time": time,
                "exercise": exercise_name.title(),
                "duration": duration,
                "calories": calories,
            }
        write_to_google_docs(exercise_data)


if __name__ == "__main__":
    start_app()
