from sqlalchemy.orm import Session
from app.repositories.url_repository import URLRepository

class StatsService:
    def __init__(self, db: Session):
        self.url_repository = URLRepository(db)

    def get_stats(self, short_key: str):
        return self.url_repository.get_stats(short_key)
