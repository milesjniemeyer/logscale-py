import logging
from logscale_py.rest_adapter import RestAdapter
from logscale_py.exceptions import LogScalePyException
from logscale_py.models import *

class LogScaleApi:
    def __init__(self, hostname: str, api_token: str, version: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_token, version, ssl_verify, logger)

    def basic_query(self, repo: str, query_string: str, start: str = '7days', end: str = 'now'):
        data = {'queryString': query_string,
                'start': start,
                'end': end}
        result = self._rest_adapter.post(endpoint=f'repositories/{repo}/query', data=data)
        return result.data