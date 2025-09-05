from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()


class DataManager:
    def __init__(self):
        self.sheety_project_id = environ.get("FLIGHT_SEARCH_GOOGLE_DOC_ID")
        self.sheety_endpoint = f"https://api.sheety.co/{self.sheety_project_id}/flightDeals"
        self.sheety_bearer_auth_token = environ.get("SHEETY_BEARER_AUTH_TOKEN")
        self.prices_page_name = "prices"
        self.users_page_name = "users"

    def get_google_doc_data(self):
        sheety_headers = {
            "Authorization": self.sheety_bearer_auth_token,
        }
        sheet_data = requests.get(f"{self.sheety_endpoint}/{self.prices_page_name}", headers=sheety_headers)
        print(f"get_google_doc_data: {sheet_data.status_code}")
        return sheet_data.json()

    def update_google_doc_record(self, record) -> None:
        sheety_headers = {
            "Authorization": self.sheety_bearer_auth_token,
        }
        response = requests.put(f"{self.sheety_endpoint}/{self.prices_page_name}/{record["id"]}", headers=sheety_headers, json={"prices": record})
        print(f"update_google_doc_record: {response.status_code}")
        print(response.text)

    def get_customer_emails(self):
        sheety_headers = {
            "Authorization": self.sheety_bearer_auth_token,
        }
        response = requests.get(f"{self.sheety_endpoint}/{self.users_page_name}", headers=sheety_headers)
        print(f"get_customer_emails: {response.status_code}")
        print(response.text)
        return response.json()
