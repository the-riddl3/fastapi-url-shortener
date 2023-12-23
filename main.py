import hashlib

from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel, HttpUrl
import sqlite3

from sqlalchemy.orm import Session

import crud
import models
import schemas
from config import HASH_LENGTH
from database import engine, SessionLocal
from schemas import UrlCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten", response_model=schemas.Url)
async def shorten(url: UrlCreate = Body(), db: Session = Depends(get_db)):
    target_url = url.url.unicode_string().encode()

    slug = hashlib.sha256(target_url) \
                     .hexdigest()[:HASH_LENGTH]

    shortened_url = crud.get_shortened_url(db, slug)

    if not shortened_url:
        shortened_url = crud.create_shortened_url(db, url, slug)

    return shortened_url


@app.get("/{slug}", response_model=schemas.Url)
async def go(slug: str, db: Session = Depends(get_db)):
    shortened_url = crud.get_shortened_url(db, slug)
    return shortened_url


