import json
import logging
import requests
import requests.packages
from json import JSONDecodeError
from typing import List, Dict
from logscale_py.exceptions import LogScalePyException
from logscale_py.models import Result

class RestAdapter:
    def __init__(self, hostname: str, api_token: str, version: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter
        :param hostname: The hostname of the LogScale instance
        :param api_token: The user's API token found under account in LogScale
        :param version: (optional) The version of the API. Normally, set to 'v1'
        :param ssl_verify: (optional) Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self.url = 'https://{}/api/{}/'.format(hostname, version)
        self._api_token = api_token
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()
        self._logger = logger or logging.getLogger(__name__)

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        full_url = self.url + endpoint
        headers = {'Authorization': f'Bearer {self._api_token}', 'Accept': 'application/json'}
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify, headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise LogScalePyException('Request failed') from e
        
        # Deserialize the JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=(log_line_post.format(False, None, e)))
            raise LogScalePyException('Bad JSON in response') from e
        
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=(log_line))
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=(log_line))
        raise LogScalePyException(f'{response.status_code}: {response.reason}')

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        """
        GET HTTP method
        :param endpoint: The endpoint on the LogScale API beging accessed
        :ep_params: Parameters to be passed in the URL query string
        """
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        """
        POST HTTP method
        :param endpoint: The endpoint on the LogScale API beging accessed
        :param ep_params: Parameters to be passed in the URL query string
        :param data: Parameters to be passed in the body of the request
        """
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)
    
    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        """
        DELETE HTTP method
        :param endpoint: The endpoint on the LogScale API beging accessed
        :param ep_params: Parameters to be passed in the URL query string
        :param data: Parameters to be passed in the body of the request
        """
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)