import os
import logging
from server.db.manager import find_long_url, insert_short_url, get_short_url_counter, increment_short_url_counter

log = logging.getLogger(__name__)


class UrlShortner:
    def __init__(self):
        self.url_allowed_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._~'
        self.domain_name = os.getenv('DOMAIN_NAME', 'www.shorter.com')

    async def get_short_url(self, url, session=None):
        existing_url_data = await find_long_url(url, session)
        if existing_url_data:
            shortened_url_id = existing_url_data['short_url_id']
        else:
            shortened_url_id = self.base_encode(await get_short_url_counter(session))
            await insert_short_url(shortened_url_id, url, session)
            await increment_short_url_counter(session)

        shortened_url = f'http://{self.domain_name}/{shortened_url_id}'
        return shortened_url

    def base_encode(self, value: int):
        base_num = len(self.url_allowed_chars)
        encoding = ''
        while value > 0:
            encoding = self.url_allowed_chars[value % base_num] + encoding
            value //= base_num
        return encoding
