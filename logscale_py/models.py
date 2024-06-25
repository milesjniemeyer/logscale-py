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