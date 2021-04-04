import logging
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_302_FOUND

from server.db.manager import find_short_url
from fastapi.responses import RedirectResponse

log = logging.getLogger(__name__)

router = APIRouter()


@router.get('/{short_url_id}')
async def retrieve_original_url(short_url_id):
    document = await find_short_url(short_url_id)
    if not document:
        raise HTTPException(status_code=404, detail="Given short url does not exist")
    else:
        long_url = document['long_url']
    return RedirectResponse(url=long_url, status_code=HTTP_302_FOUND)
