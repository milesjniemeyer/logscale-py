import requests
from requests.exceptions import RequestException
from unittest import TestCase, mock
from logscale_py.exceptions import LogScalePyException
from logscale_py.models import Result
from logscale_py.rest_adapter import RestAdapter

class TestRestAdapter(TestCase):
    def setUp(self):
        self.rest_adapter = RestAdapter(hostname='', api_token='')
        self.response = requests.Response()

    def test__do_good_request_returns_result(self):
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.request", return_value=self.response):
            result = self.rest_adapter._do('GET', '')
            self.assertIsInstance(result, Result)