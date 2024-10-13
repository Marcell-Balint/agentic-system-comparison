from pydantic import BaseModel, Field


class HotelSearchByCityRequest(BaseModel):
    cityCode: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="City IATA code to search for hotels",
    )
