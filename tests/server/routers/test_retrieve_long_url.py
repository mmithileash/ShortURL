import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from server.main import app

mocked_client = TestClient(app)


class TestShortUrl(unittest.TestCase):

    @patch("server.routers.retrieve_long_url.find_short_url", return_value={"long_url": "http://www.google.com"})
    def test_retrieve_original_url(self, mocked_find):
        response = mocked_client.get('/1', allow_redirects=False)
        self.assertEquals(response.status_code, 302)

    @patch("server.routers.retrieve_long_url.find_short_url", return_value=None)
    def test_retrieve_original_url_not_found(self, mocked_find):
        response = mocked_client.get('/1', allow_redirects=False)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.text, '{"detail":"Given short url does not exist"}')
