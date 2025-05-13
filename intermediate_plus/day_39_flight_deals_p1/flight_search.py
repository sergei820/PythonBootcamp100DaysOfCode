from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

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
        print(city)
        print(f"self._get_new_token(): {self._get_new_token()}")

        return 'TESTING'

    def _get_new_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)

        return response.json()["access_token"]
