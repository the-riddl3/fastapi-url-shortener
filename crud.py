from sqlalchemy.orm import Session

import models
import schemas


def create_shortened_url(db: Session, url: schemas.UrlCreate, slug: str):
    db_shortened_url = models.ShortenedUrl(slug=slug, target=url.url.unicode_string().encode(), expiration=url.expiration.value)
    db.add(db_shortened_url)
    db.commit()
    return db_shortened_url


def get_shortened_url(db: Session, slug: str):
    return db.query(models.ShortenedUrl).filter(models.ShortenedUrl.slug == slug).first()
