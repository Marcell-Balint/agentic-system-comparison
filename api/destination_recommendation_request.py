from pydantic import BaseModel, Field


class DestinationRecommendationRequest(BaseModel):
    originLocationCode: str = Field(
        ..., min_length=3, max_length=3, description="IATA code for the origin airport"
    )
    departureDate: str = Field(
        ...,
        pattern=r"\d{4}-\d{2}-\d{2}",
        description="Departure date in the format YYYY-MM-DD",
    )
    maxBudget: int = Field(
        None, description="Maximum budget in the local currency (optional)"
    )
