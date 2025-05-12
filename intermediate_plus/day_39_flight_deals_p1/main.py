from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheety_project_id = environ.get("FLIGHT_SEARCH_GOOGLE_DOC_ID")
sheety_page_name = "page1"
sheety_endpoint = f"https://api.sheety.co/{sheety_project_id}/flightDeals/{sheety_page_name}"
sheety_bearer_auth_token = environ.get("SHEETY_BEARER_AUTH_TOKEN")

def start_app():
    sheety_headers = {
        "Authorization": sheety_bearer_auth_token,
    }
    response = requests.get(sheety_endpoint, headers=sheety_headers)
    print(response.text)

if __name__ == "__main__":
    start_app()


# APIs Required
#
# Google Sheet Data Management - https://sheety.co/
#
# Amadeus Flight Search API (Free Signup, Credit Card not required) - https://developers.amadeus.com/
#
# Amadeus Flight Offer Docs - https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
#
# Amadeus How to work with API keys and tokens guide - https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
#
# Amadeus Search for Airport Codes by City name - https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference
#
# Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python


# Program Requirements
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
# with International Air Transport Association (IATA) codes for each city.
# Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
#
# Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
#
# If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message)
# to your own number using the Twilio API.
#
# The SMS should include
# the departure airport IATA code,
# destination airport IATA code,
# flight price and
# flight dates. e.g.
