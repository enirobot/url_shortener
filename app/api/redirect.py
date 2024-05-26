from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.core.models.error_response import ErrorResponse
from app.services.shortener_service import URLShortenerService
from app.core.db import get_db

router = APIRouter()

@router.get(
    path="/{short_key}",
    description="Redirect to the original URL",
    status_code=status.HTTP_301_MOVED_PERMANENTLY,
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
def redirect_to_original(short_key: str, db: Session = Depends(get_db)):
    try:
        url_service = URLShortenerService(db)
        url = url_service.url_repository.get_url_by_short_key(short_key)
        
        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
        
        url_service.url_repository.increment_visit_count(url)
        return RedirectResponse(status_code=status.HTTP_301_MOVED_PERMANENTLY, url=url.original_url)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )