import string
import secrets
from datetime import datetime, timedelta, UTC
from sqlalchemy.orm import Session
from app.repositories.url_repository import URLRepository
from app.config import settings

class URLShortenerService:
    def __init__(self, db: Session):
        self.url_repository = URLRepository(db)

    def generate_short_key(self, length: int = settings.SHORT_URL_LENGTH) -> str:
        alphabet = string.ascii_letters + string.digits
        short_key = ''.join(secrets.choice(alphabet) for _ in range(length))
        return short_key

    def create_short_url(self, original_url: str, expires_in_days: int):
        short_key = self.generate_short_key(settings.SHORT_URL_LENGTH)
        
        count = 0
        while self.url_repository.get_url_by_short_key(short_key):
            if count > settings.SHORT_KEY_RETRIES:
                raise Exception("Failed to generate a unique short key")
            short_key = self.generate_short_key(settings.SHORT_URL_LENGTH)
            count += 1
        
        expires_at = datetime.now(UTC) + timedelta(days=expires_in_days)
        return self.url_repository.create_url(original_url, short_key, expires_at)
