from sqlalchemy.orm import Session
from datetime import datetime, timezone, UTC
from app.models.url import URL

class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_url(self, original_url: str, short_key: str, expires_at: datetime):
        db_url = URL(original_url=original_url, short_key=short_key, expires_at=expires_at)
        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)
        return db_url

    def get_url_by_short_key(self, short_key: str):
        url = self.db.query(URL).filter(URL.short_key == short_key, URL.expired == False).first()
        
        if url and url.expires_at.replace(tzinfo=timezone.utc) < datetime.now(UTC):
            url.expired = True
            self.db.commit()
            self.db.refresh(url)
            return None
        
        return url

    def increment_visit_count(self, url: URL):
        url.visit_count += 1
        self.db.commit()
        self.db.refresh(url)

    def get_stats(self, short_key: str):
        url = self.get_url_by_short_key(short_key)
        return {"visit_count": url.visit_count} if url else None
