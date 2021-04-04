import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from server.main import app

mocked_client = TestClient(app)


class TestShortUrl(unittest.TestCase):
    def setUp(self) -> None:
        self.shorten_url = "/shorten_url?use_mongo_session=False"

    @patch("server.services.shorten_url.increment_short_url_counter")
    @patch("server.services.shorten_url.get_short_url_counter", return_value=1)
    @patch("server.services.shorten_url.find_long_url", return_value=None)
    @patch("server.services.shorten_url.insert_short_url")
    def test_create_short_url(self, mocked_insert, mocked_find, mock_get_short_url_counter, mock_increment_short_url_counter):
        response = mocked_client.post(self.shorten_url, json={"long_url": "http://www.google.com"})
        mocked_insert.assert_called_once()
        mock_increment_short_url_counter.assert_called_once()
        expected_response_data = {
            "short_url": "http://www.shorter.com/1"
        }
        self.assertEquals(response.json(), expected_response_data)
        assert response.status_code == 200

    @patch("server.services.shorten_url.find_long_url", return_value={'short_url_id': 'mocked_value'})
    @patch("server.services.shorten_url.insert_short_url")
    def test_create_short_url_long_url_exists(self, mocked_insert, mocked_find):
        response = mocked_client.post(self.shorten_url, json={"long_url": "http://www.google.com"})
        mocked_insert.assert_not_called()
        expected_response_data = {
            "short_url": "http://www.shorter.com/mocked_value"
        }
        self.assertEquals(response.json(), expected_response_data)
        assert response.status_code == 200

    def test_bad_given_url(self):
        response = mocked_client.post(self.shorten_url, json={"long_url": "not a http or https url"})
        self.assertEquals(response.status_code, 422)
