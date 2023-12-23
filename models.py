import sqlalchemy
from sqlalchemy import Column, String, SMALLINT

from database import Base


class ShortenedUrl(Base):
    __tablename__ = "shortened_urls"

    slug = Column(String, primary_key=True, index=True)
    target = Column(String, unique=True, index=True, nullable=False)
    expiration = Column(SMALLINT, nullable=False)

