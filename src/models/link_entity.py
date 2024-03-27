import uuid

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .base import Base


class LinkEntity(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True)
    full_url = Column(String(), unique=True, nullable=False)
    shortened_url = Column(String(), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    usages = Column(Integer, default=0)
    last_usage = Column(DateTime, default=None)
