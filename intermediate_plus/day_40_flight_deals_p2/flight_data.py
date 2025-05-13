class FlightData:
    """
    This class is responsible for structuring the flight data.
    """
    def find_cheapest_flight(self, flight_offers: dict) -> int:
        try:
            min_price = flight_offers["data"][0]["travelerPricings"][0]["price"]["total"]
            for data in flight_offers["data"]:
                price = data["travelerPricings"][0]["price"]["total"]
                if min_price > price:
                    min_price = price
        except IndexError:
            min_price = "N/A"

        return min_price