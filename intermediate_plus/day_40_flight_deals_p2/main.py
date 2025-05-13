from intermediate_plus.day_40_flight_deals_p2.data_manager import DataManager
from intermediate_plus.day_40_flight_deals_p2.flight_data import FlightData
from intermediate_plus.day_40_flight_deals_p2.flight_search import FlightSearch
from intermediate_plus.day_40_flight_deals_p2.notification_manager import NotificationManager, ADDR_TO


def start_app():
    """
    #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
    to achieve the program requirements.
    :return:
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_google_doc_data()

    flight_search = FlightSearch()
    flight_data = FlightData()
    notification_manager = NotificationManager()

    for flight in sheet_data["prices"]:
        if flight["iataCode"] == "":
            flight["iataCode"] = flight_search.get_iata_code(flight["city"])
            data_manager.update_google_doc_record(flight)

        flight_offers = flight_search.search_flight_offers(flight["iataCode"])
        min_price = flight_data.find_cheapest_flight(flight_offers)

        print(f"Getting flights for {flight["city"]}...")
        print(f"{flight["city"]}: £{min_price}")

        if min_price != 'N/A' and float(min_price) < flight['lowestPrice']:
            message = f"Low Price alert! Flight to {flight["city"]}: £{min_price}"
            print(message)
            notification_manager.send_email(ADDR_TO, message)





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
