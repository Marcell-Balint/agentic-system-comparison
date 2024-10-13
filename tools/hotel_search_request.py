from pydantic import BaseModel, Field, field_validator


class HotelSearchRequest(BaseModel):
    cityCode: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="City IATA code for the hotel location",
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
    number_of_adults: int = Field(..., gt=0, description="Number of adult guests")

    @field_validator("checkInDate", "checkOutDate")
    def validate_dates(cls, value, field):
        from datetime import datetime

        date = datetime.strptime(value, "%Y-%m-%d")
        if date < datetime.now():
            raise ValueError(f"{field.name} cannot be in the past")
        return value
