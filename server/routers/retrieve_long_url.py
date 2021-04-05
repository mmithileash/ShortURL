import logging
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_302_FOUND

from server.db.manager import find_short_url
from fastapi.responses import RedirectResponse

log = logging.getLogger(__name__)

router = APIRouter()


@router.get('/{short_url_id}')
async def retrieve_original_url(short_url_id):
    """
    Retrieves the original url and redirects appropriately using the index given.
    """""

    document = await find_short_url(short_url_id)
    if not document:
        log.info(f'Document not found for index:{short_url_id}')
        raise HTTPException(status_code=404, detail="Given short url does not exist")

    long_url = document['long_url']
    log.info(f'Document found for index:{short_url_id} and the corresponding URL is: {long_url}')
    return RedirectResponse(url=long_url, status_code=HTTP_302_FOUND)
