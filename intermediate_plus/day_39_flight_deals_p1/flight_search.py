from datetime import datetime, timedelta
from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

get_cities_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
get_flight_offers_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

originLocationCode = "LON"

class FlightSearch:
    """ This class is responsible for talking to the Flight Search API """
    def __init__(self):
        self._api_key = environ.get("AMADEUS_API_KEY")
        self._api_secret = environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def get_iata_code(self, city: str) -> str:
        """
        In order to search for flights, we need an International Air Transport Association (IATA) code.
        This code helps to identify airports and metropolitan areas.
        :param city: str
        :return: iata_code: str
        """
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city,
            "max": "1"
        }
        response = requests.get(url=get_cities_endpoint, headers=headers, params=params)
        response.raise_for_status()

        iata_code = response.json()["data"][0]["iataCode"]

        return iata_code

    def _get_new_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)

        return response.json()["access_token"]

    def search_flight_offers(self, iata_code: str):
        departure_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")  # 2017-12-25
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "originLocationCode": originLocationCode,
            "destinationLocationCode": iata_code,
            "departureDate": departure_date,
            "nonStop": "true",
            "adults": "1",
            "currencyCode": "GBP",
        }
        # print(params)
        response = requests.get(url=get_flight_offers_endpoint, headers=headers, params=params)
        # print(response.status_code)
        # print(response.text)

        return response.json()
