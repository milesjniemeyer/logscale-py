from typing import List, Dict

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """
        Constructor for Result
        :param status_code: The HTTP status code
        :param message: The message to return with the response
        :param data: The data to return with the response
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []