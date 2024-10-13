from pydantic import BaseModel, Field
from typing import List


class HotelSearchRequest(BaseModel):
    hotelIds: List[str] = Field(
        ..., min_items=1, description="List of Amadeus property codes (8 characters)"
    )
    checkInDate: str = Field(
        ...,
        pattern=r"\d{4}-\d{2}-\d{2}",
        description="Check-in date in the format YYYY-MM-DD",
    )
    checkOutDate: str = Field(
        ...,
        pattern=r"\d{4}-\d{2}-\d{2}",
        description="Check-out date in the format YYYY-MM-DD",
    )
    number_of_adults: int = Field(
        ..., gt=0, le=9, description="Number of adult guests (1-9)"
    )
