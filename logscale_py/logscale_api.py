import logging
from logscale_py.rest_adapter import RestAdapter
from logscale_py.exceptions import LogScalePyException
from logscale_py.models import *

class LogScaleAPI:
    def __init__(self, hostname: str, api_token: str, version: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_token, version, ssl_verify, logger)

    def query(self, repo: str, query_string: str, allow_event_skipping: bool = False, arguments: Dict = None, end: str = 'now', ingest_end: str = None, ingest_start: str = None, language_version: str = None, start: str = '24hours', time_zone_offset_minutes: int = None) -> QueryList:
        data = {'allowEventSkipping': allow_event_skipping,
                'arguments': arguments,
                'end': end,
                'ingestEnd': ingest_end,
                'ingestStart': ingest_start,
                'isLive': False,
                'languageVersion': language_version,
                'queryString': query_string,
                'start': start,
                'timeZoneOffsetMinutes': time_zone_offset_minutes}
        result = self._rest_adapter.post(endpoint=f'/repositories/{repo}/query', data=data)
        return QueryList([Query.from_dict(item) for item in result.data])