from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.models.error_response import ErrorResponse
from app.schemas.stats import StatsResponse
from app.services.stats_service import StatsService
from app.core.db import get_db

router = APIRouter()

@router.get(
    path="/stats/{short_key}",
    response_model=StatsResponse,
    description="Get URL stats",
    status_code=status.HTTP_200_OK,
    responses={
        404: {
            "model": ErrorResponse,
            "description": "URL not found"
        },
        500: {
            "model": ErrorResponse,
            "description": "Internal Server Error"
        }
    }
)
def get_url_stats(short_key: str, db: Session = Depends(get_db)):
    stats_service = StatsService(db)
    stats = stats_service.get_stats(short_key)
    
    if not stats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    return stats
