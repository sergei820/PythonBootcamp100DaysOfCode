from datetime import datetime
from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

USERNAME = environ.get("PIXELA_USERNAME")
TOKEN = environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

def start_app():


    pixela_endpoint = "https://pixe.la/v1/users"
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)



    graph_config = {
        "id": GRAPH_ID,
        "name": "Running Graph",
        "unit": "Km",
        "type": "float",
        "color": "shibafu"
    }

    headers = {
        "X-USER-TOKEN": TOKEN,
    }

    # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)

    today = datetime.now()
    print(today.strftime("%Y%m%d"))
    print(USERNAME)

    post_pixel_body = {
        "date": today.strftime("%Y%m%d"),  # "20250509",
        "quantity": "1"
    }
    # response = requests.post(url=pixel_endpoint, json=post_pixel_body, headers=headers)
    # print(response.text)

    date = today.strftime("%Y%m%d")
    update_pixel_endpoint = f"{pixel_endpoint}/{date}"

    pixel_updated_body = {"quantity": "2"}
    # response = requests.put(url=update_pixel_endpoint, json=pixel_updated_body, headers=headers)
    # print(response.status_code)
    # print(response.text)

    response = requests.delete(url=update_pixel_endpoint, headers=headers)
    print(response.text)


if __name__ == "__main__":
    start_app()
