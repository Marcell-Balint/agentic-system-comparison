import os

from destination_recommendation_request import DestinationRecommendationRequest
from flight_offer_request import FlightOfferRequest
from hotel_search_request import HotelSearchRequest

from amadeus import Client, ResponseError


class TravelAPI:
    def __init__(self) -> None:
        self.amadeus_client = Client(
            client_id=os.getenv("AMADEUS_CLIENT_ID"),
            client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
        )

    def find_flight_offers(
        self,
        flight_request: FlightOfferRequest,  # Use Pydantic model for input validation
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

    # New function to check hotel availability
    def check_hotel_availability(
        self,
        hotel_request: HotelSearchRequest,  # Use Pydantic model for input validation
    ) -> str:
        try:
            # Call the hotel search API endpoint
            response = self.amadeus_client.shopping.hotel_offers.get(
                cityCode=hotel_request.cityCode,
                checkInDate=hotel_request.checkInDate,
                checkOutDate=hotel_request.checkOutDate,
                adults=hotel_request.number_of_adults,
            )
            print(response.data)
        except ResponseError as error:
            print(error)

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
