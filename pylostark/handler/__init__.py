import requests
from ..logger import logger


class ApiRequestHandler:
    def __init__(self, pylostark):
        self.pylostark = pylostark

    def _request(self, method, path, params=None):
        url = f'{self.pylostark._url}{path}'
        response = requests.request(method, url, headers=self.pylostark.headers, params=params)
        if not (200 <= response.status_code < 300):
            logger.error(f'{method} {url} {params} {response.status_code}')
        else:
            logger.debug(f'{method} {url} {params} {response.status_code}')
        return response.json()

    def _get(self, path, params=None):
        return self._request('GET', path, params=params)

