import logging
from fastapi import APIRouter

from server.models.url_creater import ShortenUrlRequest, ShortenUrlResponse

log = logging.getLogger(__name__)

router = APIRouter()


@router.post('/shorten_url', response_model=ShortenUrlResponse)
async def create_short_url(short_url_request: ShortenUrlRequest):
    pass
