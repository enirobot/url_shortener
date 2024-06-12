from datetime import datetime, timedelta, UTC
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.core.db import Base


class URL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_key = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))
    expires_at = Column(DateTime, default=lambda: datetime.now(UTC) + timedelta(days=7))
    visit_count = Column(Integer, default=0)
    expired = Column(Boolean, default=False)
