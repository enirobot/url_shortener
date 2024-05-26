from pydantic import BaseModel, Field

class URLCreate(BaseModel):
    url: str = Field(description="URL to be shortened")
    expires_in_days: int = Field(7, description="Number of days the URL will be active")

class URLResponse(BaseModel):
    short_url: str = Field(description="Shortened URL")