from pydantic import HttpUrl, BaseModel

import enums


class UrlCreate(BaseModel):
    url: HttpUrl
    expiration: enums.Expiration

    class Config:
        orm_mode = True


class Url(BaseModel):
    slug: str
    target: HttpUrl
    expiration: enums.Expiration
