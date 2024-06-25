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
    def __init__(self, **kwargs: Any):
        self.data: Dict = kwargs
    
    @classmethod
    def from_dict(cls, data_dict: Dict) -> 'Query':
        return cls(**data_dict)
    
class QueryList(list):
    @property
    def data(self):
        return [query.data for query in self]
    
class QueryJob():
    def __init__(self, data):
        """
        Constructor for QueryJobResponse
        :param data: Python Dictionary containing the response data
        """
        self.hashed_query_on_view = data.get('hashedQueryOnView')
        self.id = data.get('id')
        self.query_on_view = data.get('queryOnView')
        self.static_meta_data = data.get('staticMetaData')
        self.execution_mode = self.static_meta_data.get('executionMode') if self.static_meta_data else None

    def __str__(self):
        return f'QueryJob(hashed_query_on_view={self.hashed_query_on_view}, id={self.id}, query_on_view={self.query_on_view}, static_meta_data={self.static_meta_data}, execution_mode={self.execution_mode})'