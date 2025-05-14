from intermediate_plus.day_40_flight_deals_p2.data_manager import DataManager
from intermediate_plus.day_40_flight_deals_p2.flight_data import FlightData
from intermediate_plus.day_40_flight_deals_p2.flight_search import FlightSearch
from intermediate_plus.day_40_flight_deals_p2.notification_manager import NotificationManager


def start_app():
    """
    #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
    to achieve the program requirements.
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_google_doc_data()
    direct_flight = True

    flight_search = FlightSearch()
    flight_data = FlightData()
    notification_manager = NotificationManager()

    emails_list = [user["whatIsYoursEmail?"] for user in data_manager.get_customer_emails()["users"]]
    print(f"emails_list: {emails_list}")

    for flight in sheet_data["prices"]:
        if flight["iataCode"] == "":
            flight["iataCode"] = flight_search.get_iata_code(flight["city"])
            data_manager.update_google_doc_record(flight)

        flight_offers = flight_search.search_flight_offers(iata_code=flight["iataCode"])
        min_price = flight_data.find_cheapest_flight(flight_offers)

        print(f"Getting flights to {flight["city"]}...")
        print(f"{flight["city"]}: £{min_price}")

        if min_price == 'N/A':
            direct_flight = False
            flight_offers = flight_search.search_flight_offers(iata_code=flight["iataCode"], flight_without_stops="false")
            min_price = flight_data.find_cheapest_flight(flight_offers)
            print(f"Getting connecting flights to {flight["city"]}...")
            print(f"{flight["city"]}: £{min_price}")
            # Getting flights to Tokyo...
            # Tokyo: £N/A
            # Getting connecting flights to Tokyo...
            # Tokyo: £522.92

        elif float(min_price) < flight['lowestPrice']:
            message = f"Low Price alert! Direct flight to {flight["city"]}: £{min_price}"
            if not direct_flight:
                message = f"Low Price alert! Connected flight to {flight["city"]}: £{min_price}"
            print(message)
            notification_manager.send_emails(emails_list, message)


if __name__ == "__main__":
    start_app()
