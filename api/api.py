import os
from amadeus import Client, ResponseError
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List

# Create a global Amadeus client
amadeus_client = Client(
    client_id=os.getenv("AMADEUS_CLIENT_ID"),
    client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
)

# Pydantic model for FlightOfferRequest
class FlightOfferRequest(BaseModel):
    originLocationCode: str = Field(
        ..., min_length=3, max_length=3, description="IATA code for the origin airport"
    )
    destinationLocationCode: str = Field(
        ..., min_length=3, max_length=3, description="IATA code for the destination airport"
    )
    departureDate: str = Field(
        ..., pattern=r"\d{4}-\d{2}-\d{2}", description="Departure date in the format YYYY-MM-DD"
    )
    number_of_adults: int = Field(..., gt=0, description="Number of adult passengers")

    @field_validator("departureDate")
    def validate_departure_date(cls, value):
        from datetime import datetime
        dep_date = datetime.strptime(value, "%Y-%m-%d")
        if dep_date < datetime.now():
            raise ValueError("Departure date cannot be in the past")
        return value

# Find flight offers
def find_flight_offers(data: dict) -> str:
    """
    Find flight offers based on the provided input parameters.

    Args:
        data (dict): A dictionary containing:
            - originLocationCode (str): IATA code for the origin airport (3 characters).
            - destinationLocationCode (str): IATA code for the destination airport (3 characters).
            - departureDate (str): Departure date in the format YYYY-MM-DD.
            - number_of_adults (int): Number of adult passengers (> 0).

    Returns:
        str: The response data from the Amadeus flight offer search API.
    """
    try:
        flight_request = FlightOfferRequest(**data)
        response = amadeus_client.shopping.flight_offers_search.get(
            originLocationCode=flight_request.originLocationCode,
            destinationLocationCode=flight_request.destinationLocationCode,
            departureDate=flight_request.departureDate,
            adults=flight_request.number_of_adults,
        )
        return response.data

    except ValidationError as ve:
        return f"Validation error: {ve}"

    except ResponseError as error:
        return f"API error: {error}"


# Pydantic model for HotelSearchByCityRequest
class HotelSearchByCityRequest(BaseModel):
    cityCode: str = Field(..., min_length=3, max_length=3, description="City IATA code to search for hotels")

# Find hotels in a city
def find_hotels_in_city(data: dict) -> str:
    """
    Find hotels in a city based on the provided input parameters.

    Args:
        data (dict): A dictionary containing:
            - cityCode (str): IATA code for the city (3 characters).

    Returns:
        str: The response data from the Amadeus hotel search by city API.
    """
    try:
        hotel_request = HotelSearchByCityRequest(**data)
        response = amadeus_client.reference_data.locations.hotels.by_city.get(
            cityCode=hotel_request.cityCode
        )
        return response.data

    except ValidationError as ve:
        return f"Validation error: {ve}"

    except ResponseError as error:
        return f"API error: {error}"


# Pydantic model for HotelSearchRequest
class HotelSearchRequest(BaseModel):
    hotelIds: List[str] = Field(..., min_items=1, description="List of Amadeus property codes")
    checkInDate: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}", description="Check-in date in the format YYYY-MM-DD")
    checkOutDate: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}", description="Check-out date in the format YYYY-MM-DD")
    number_of_adults: int = Field(..., gt=0, le=9, description="Number of adult guests (1-9)")

# Check hotel availability
def check_hotel_availability(data: dict) -> str:
    """
    Check hotel availability based on the provided input parameters.

    Args:
        data (dict): A dictionary containing:
            - hotelIds (list of str): List of Amadeus property codes.
            - checkInDate (str): Check-in date in the format YYYY-MM-DD.
            - checkOutDate (str): Check-out date in the format YYYY-MM-DD.
            - number_of_adults (int): Number of adult guests (1-9).

    Returns:
        str: The response data from the Amadeus hotel availability search API.
    """
    try:
        hotel_request = HotelSearchRequest(**data)
        response = amadeus_client.shopping.hotel_offers_search.get(
            hotelIds=hotel_request.hotelIds,
            checkInDate=hotel_request.checkInDate,
            checkOutDate=hotel_request.checkOutDate,
            adults=hotel_request.number_of_adults,
        )
        return response.data

    except ValidationError as ve:
        return f"Validation error: {ve}"

    except ResponseError as error:
        return f"API error: {error}"


# Pydantic model for DestinationRecommendationRequest
class DestinationRecommendationRequest(BaseModel):
    originLocationCode: str = Field(..., min_length=3, max_length=3, description="IATA code for the origin airport")
    departureDate: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}", description="Departure date in the format YYYY-MM-DD")
    maxBudget: int = Field(None, description="Maximum budget in local currency (optional)")

# Recommend destinations
def recommend_destinations(data: dict) -> str:
    """
    Recommend destinations based on the provided input parameters.

    Args:
        data (dict): A dictionary containing:
            - originLocationCode (str): IATA code for the origin airport (3 characters).
            - departureDate (str): Departure date in the format YYYY-MM-DD.
            - maxBudget (int, optional): Maximum budget in local currency.

    Returns:
        str: The response data from the Amadeus flight destination recommendation API.
    """
    try:
        recommendation_request = DestinationRecommendationRequest(**data)
        response = amadeus_client.shopping.flight_destinations.get(
            origin=recommendation_request.originLocationCode,
            departureDate=recommendation_request.departureDate,
            maxPrice=recommendation_request.maxBudget,
        )
        return response.data

    except ValidationError as ve:
        return f"Validation error: {ve}"

    except ResponseError as error:
        return f"API error: {error}"
