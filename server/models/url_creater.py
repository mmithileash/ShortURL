from pydantic import BaseModel, AnyHttpUrl


class ShortenUrlRequest(BaseModel):
    long_url: AnyHttpUrl


class ShortenUrlResponse(BaseModel):
    short_url: AnyHttpUrl