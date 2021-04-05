import logging
from fastapi import APIRouter

from server.db import mongo_client
from server.models.url_creater import ShortenUrlRequest, ShortenUrlResponse
from server.services.shorten_url import UrlShortner

log = logging.getLogger(__name__)

router = APIRouter()


@router.post('/shorten_url', response_model=ShortenUrlResponse)
async def create_short_url(short_url_request: ShortenUrlRequest, use_mongo_session: bool = True):
    """
    Takes the given URL request and returns a shorter indexed URL. This index can be used to retrieve the
    original URL again.
    """""
    long_url = short_url_request.long_url
    s = None
    if use_mongo_session:
        # Hack here as tests will not be able to run using mongo session
        # Current mongo mocking frameworks does not allow mocking sessions and when using mongo with async
        s = await mongo_client.start_session()

    short_url = await UrlShortner().get_short_url(long_url, s)
    log.info(f'short url is: {short_url}')

    if use_mongo_session:
        s.end_session()

    return ShortenUrlResponse(short_url=short_url)
