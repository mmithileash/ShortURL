import logging
from fastapi import APIRouter

from server.db import mongo_client
from server.models.url_creater import ShortenUrlRequest, ShortenUrlResponse
from server.services.shorten_url import UrlShortner

log = logging.getLogger(__name__)

router = APIRouter()


@router.post('/shorten_url', response_model=ShortenUrlResponse)
async def create_short_url(short_url_request: ShortenUrlRequest):
    long_url = short_url_request.long_url
    with await mongo_client.start_session() as s:
        short_url = await UrlShortner().get_short_url(long_url, s)
        log.info(f'short url is: {short_url}')

    return ShortenUrlResponse(short_url=short_url)
