import os

from .destination_recommendation_request import DestinationRecommendationRequest
from .flight_offer_request import FlightOfferRequest
from .hotel_search_request import HotelSearchRequest
from .hotel_search_by_city_request import HotelSearchByCityRequest

from amadeus import Client, ResponseError


class TravelAPI:
    def __init__(self) -> None:
        self.amadeus_client = Client(
            client_id=os.getenv("AMADEUS_CLIENT_ID"),
            client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
        )

    def find_flight_offers(
        self,
        flight_request: FlightOfferRequest,
    ) -> str:
        try:
            response = self.amadeus_client.shopping.flight_offers_search.get(
                originLocationCode=flight_request.originLocationCode,
                destinationLocationCode=flight_request.destinationLocationCode,
                departureDate=flight_request.departureDate,
                adults=flight_request.number_of_adults,
            )
            print(response.data)
        except ResponseError as error:
            print(error)

    def find_hotels_in_city(self, hotel_request: HotelSearchByCityRequest) -> str:
        try:
            response = self.amadeus_client.reference_data.locations.hotels.by_city.get(
                cityCode=hotel_request.cityCode
            )

            print(response.data)
        except ResponseError as error:
            print(error)

    def check_hotel_availability(
        self,
        hotel_request: HotelSearchRequest,  # Use Pydantic model for input validation
    ) -> str:
        try:
            # Call the Amadeus API to search for hotel offers using only required parameters
            response = self.amadeus_client.shopping.hotel_offers_search.get(
                hotelIds=hotel_request.hotelIds,
                checkInDate=hotel_request.checkInDate,
                checkOutDate=hotel_request.checkOutDate,
                adults=hotel_request.number_of_adults,
            )

            # Print the response data (or process it as needed)
            print(response.data)
        except ResponseError as error:
            print(f"Error: {error}")

    def recommend_destinations(
        self, recommendation_request: DestinationRecommendationRequest
    ) -> str:
        try:
            response = self.amadeus_client.shopping.flight_destinations.get(
                origin=recommendation_request.originLocationCode,
                departureDate=recommendation_request.departureDate,
                maxPrice=recommendation_request.maxBudget,
            )
            print(response.data)
        except ResponseError as error:
            print(error)
