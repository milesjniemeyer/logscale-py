import logging
from logscale_py.rest_adapter import RestAdapter
from logscale_py.exceptions import LogScalePyException
from logscale_py.models import *

class LogScaleAPI:
    def __init__(self, hostname: str, api_token: str, version: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_token, version, ssl_verify, logger)

    def query(self, repo: str, query_string: str, allow_event_skipping: bool = False, arguments: Dict = None, end: str = 'now', ingest_end: str = None, ingest_start: str = None, language_version: str = None, start: str = '24hours', time_zone_offset_minutes: int = None) -> Query:
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
        return Query(result.data)
    
    def query_job(self, repo: str, query_string: str, event_id: str = None, number_of_events_after: int = None, number_of_events_before: int = None, timestamp: int = None, allow_event_skipping: bool = False, arguments: Dict = None, around: str = None, auto_bucket_count: int = None, end: str = 'now', include_delete_events: bool = None, ingest_end: str = None, ingest_start: str = None, is_alert_query: bool = None, is_interactive: bool = False, is_live: bool = False, is_repeating_subquery: bool = False, language_version: str = None, no_result_until_done: bool = False, show_query_event_distribution: bool = False, start: str = '24hours', time_zone: str = None, time_zone_offset_minutes: int = None, use_ingest_time: bool = False) -> QueryJob:
        data = {'allowEventSkipping': allow_event_skipping,
                'arguments': arguments,
                'around': around,
                'eventId': event_id,
                'numberOfEventsAfter': number_of_events_after,
                'numberOfEventsBefore': number_of_events_before,
                'timestamp': timestamp,
                'autoBucketCount': auto_bucket_count,
                'end': end,
                'includeDeletedEvents': include_delete_events,
                'ingestEnd': ingest_end,
                'ingestStart': ingest_start,
                'isAlertQuery': is_alert_query,
                'isInterative': is_interactive,
                'isLive': is_live,
                'isRepeatingSubquery': is_repeating_subquery,
                'languageVersion': language_version,
                'noResultUntilDone': no_result_until_done,
                'queryString': query_string,
                'showQueryEventDistribution': show_query_event_distribution,
                'start': start,
                'time_zone': time_zone,
                'timeZoneOffsetMinutes': time_zone_offset_minutes}
        result = self._rest_adapter.post(endpoint=f'/repositories/{repo}/queryjobs', data=data)
        return QueryJob(result.data)
    
    def poll_query(self, repo: str, id: str):
        result = self._rest_adapter.get(endpoint=f'/repositories/{repo}/queryjobs/{id}')
        return result.data