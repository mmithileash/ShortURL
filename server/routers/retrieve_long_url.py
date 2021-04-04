import logging
from fastapi import APIRouter

log = logging.getLogger(__name__)

router = APIRouter()


@router.get('/{short_url_id}')
async def retrieve_original_url(short_url_id):
    pass
