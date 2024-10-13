from pydantic import BaseModel, Field, field_validator


class FlightOfferRequest(BaseModel):
    originLocationCode: str = Field(
        ..., min_length=3, max_length=3, description="IATA code for the origin airport"
    )
    destinationLocationCode: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="IATA code for the destination airport",
    )
    departureDate: str = Field(
        ...,
        regex=r"\d{4}-\d{2}-\d{2}",
        description="Departure date in the format YYYY-MM-DD",
    )
    number_of_adults: int = Field(..., gt=0, description="Number of adult passengers")

    @field_validator("departureDate")
    def validate_departure_date(cls, value):
        from datetime import datetime

        dep_date = datetime.strptime(value, "%Y-%m-%d")
        if dep_date < datetime.now():
            raise ValueError("Departure date cannot be in the past")
        return value
