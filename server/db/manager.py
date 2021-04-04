from pprint import pprint
from typing import Dict, Any

from datetime import datetime

from server.db import url_mapping_collection, short_url_counter_collection


async def insert_short_url(short_url_id, long_url, session=None) -> None:
    await url_mapping_collection.insert_one({
        'short_url_id': short_url_id,
        'long_url': long_url,
        'created_at': datetime.utcnow()
    }, session=session)


async def find_long_url(long_url, session=None) -> Dict[Any, Any]:
    document = await url_mapping_collection.find_one({"long_url": long_url}, session=session)
    return document


async def find_short_url(short_url_id, session=None) -> Dict[Any, Any]:
    document = await url_mapping_collection.find_one({"short_url_id": short_url_id}, session=session)
    return document


async def get_short_url_counter(session=None) -> int:
    document = await short_url_counter_collection.find_one({'_id': 'counter'}, session=session)
    if not document:
        document = await increment_short_url_counter()

    return document['value']


async def increment_short_url_counter(session=None) -> None:
    await short_url_counter_collection.find_one_and_update(
        {'_id': 'counter'}, {'$inc': {'value': 1}}, upsert=True, session=session
    )
