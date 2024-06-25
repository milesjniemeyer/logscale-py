from typing import Any, Dict, List

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """
        Constructor for Result
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class Query:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return str(self.data)
    
class QueryJob:
    def __init__(self, data):
        self.data = data
        self.hashed_query_on_view = data.get('hashedQueryOnView')
        self.id = data.get('id')
        self.query_on_view = data.get('queryOnView')
        self.static_meta_data = data.get('staticMetaData')
        self.execution_mode = self.static_meta_data.get('executionMode') if self.static_meta_data else None

    def __str__(self):
        return str(self.data)
    
class PollQuery:
    def __init__(self, data):
        self.data = data
        self.cancelled = data.get('cancelled')
        self.done = data.get('done')
        self.events = Query(data.get('events')) if data.get('events') else None
        self.filter_matches = data.get('filterMatches')
        self.meta_data = data.get('metaData')
        self.query_event_distribution = data.get('queryEventDistribution')
        self.warnings = data.get('warnings')

    def __str__(self):
        return str(self.data)