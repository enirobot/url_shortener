from pydantic import BaseModel, Field

class StatsResponse(BaseModel):
    visit_count: int = Field(0, description="Number of visits to the URL")