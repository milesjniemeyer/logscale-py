from typing import Dict, List

class Result:
    """
    Simple response model to handle all returned data from the REST adapter
    :param status_code: Standard HTTP Status code
    :param message: Human readable result
    :param data: Python list of dictionaries (or maybe just a single dictionary on error)
    """
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class Search:
    """
    This class represents a Search object
    :param data: The list of dictionaries returned upon calling the search endpoint
    """
    def __init__(self, data: List[Dict]):
        self.data = data
    
    def __str__(self):
        return str(self.data)
    
class CreateQueryJob:
    """
    This class represents a CreateQueryJob object
    :param data: The list of dictionaries returned upon calling the create_query_job endpoint
    """
    def __init__(self, data: Dict):
        self.data = data
        self.hashed_query_on_view = data.get('hashedQueryOnView')
        self.id = data.get('id')
        self.query_on_view = data.get('queryOnView')
        self.static_meta_data = data.get('staticMetaData')
        self.execution_mode = self.static_meta_data.get('executionMode') if self.static_meta_data else None

    def __str__(self):
        return str(self.data)
    
class PollQueryJob:
    """
    This class represents a PollQueryJob object
    :param data: The list of dictionaries returned upon calling the create_query_job endpoint
    """
    def __init__(self, data: List[Dict]):
        self.data = data
        self.cancelled = data.get('cancelled')
        self.done = data.get('done')
        self.events = Search(data.get('events')) if data.get('events') else None
        self.filter_matches = data.get('filterMatches')
        self.meta_data = data.get('metaData')
        self.query_event_distribution = data.get('queryEventDistribution')
        self.warnings = data.get('warnings')

    def __str__(self):
        return str(self.data)
    
class DeleteQueryJob:
    """
    This class represents a DeleteQueryJob object.
    :param status_code: The status code of the response from the Result class.
    """
    def __init__(self, status_code: int):
        self.status_code = status_code

    def __str__(self):
        return str(f'Query job successfully deleted.')