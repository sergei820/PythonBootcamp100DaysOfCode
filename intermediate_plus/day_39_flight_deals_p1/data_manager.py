from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

sheety_project_id = environ.get("FLIGHT_SEARCH_GOOGLE_DOC_ID")
sheety_page_name = "page1"
sheety_endpoint = f"https://api.sheety.co/{sheety_project_id}/flightDeals/{sheety_page_name}"
sheety_bearer_auth_token = environ.get("SHEETY_BEARER_AUTH_TOKEN")

class DataManager:

    def get_google_doc_data(self):
        sheety_headers = {
            "Authorization": sheety_bearer_auth_token,
        }
        sheet_data = requests.get(sheety_endpoint, headers=sheety_headers)
        return sheet_data.json()

    def update_google_doc_record(self, record) -> None:
        sheety_headers = {
            "Authorization": sheety_bearer_auth_token,
        }
        response = requests.put(f"{sheety_endpoint}/{record["id"]}", headers=sheety_headers, json={"page1": record})
        print(response.text)
