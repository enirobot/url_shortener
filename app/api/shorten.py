from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.models.error_response import ErrorResponse
from app.schemas.url import URLCreate, URLResponse
from app.services.shortener_service import URLShortenerService
from app.core.db import get_db
from app.config import settings

router = APIRouter()

@router.post(
    path="/shorten", 
    response_model=URLResponse,
    description="Create a short URL",
    status_code=status.HTTP_201_CREATED,
    responses={
        500: {
            "model": ErrorResponse,
            "description": "Internal Server Error"
        }
    }
)
def create_short_url(url_create: URLCreate, db: Session = Depends(get_db)):
    try:
        url_service = URLShortenerService(db)
        url = url_service.create_short_url(url_create.url, url_create.expires_in_days)
        return URLResponse(short_url=f"{settings.BASE_URL}/{url.short_key}")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )