import requests
from requests import Response

class ApiRequest:
    def __init__(self, url: str) -> None:
        if not url:
            raise ValueError('url is a required parameter')
        self.url = url.rstrip('/')

    def get(self, url_params: dict[str, str] | None = None, **kwargs) -> Response:
        url = self._build_url(url_params)
        return requests.get(url, **kwargs)

    def post(self, url_params: dict[str, str] | None = None, **kwargs) -> Response:
        url = self._build_url(url_params)
        return requests.post(url, **kwargs)

    def put(self, url_params: dict[str, str] | None = None, **kwargs) -> Response:
        url = self._build_url(url_params)
        return requests.put(url, **kwargs)

    def delete(self, url_params: dict[str, str] | None = None, **kwargs) -> Response:
        url = self._build_url(url_params)
        return requests.delete(url, **kwargs)

    def head(self, url_params: dict[str, str] | None = None, **kwargs) -> Response:
        url = self._build_url(url_params)
        return requests.head(url, **kwargs)

    def _build_url(self, url_params: dict[str, str] | None) -> str:
        url = self.url
        if url_params:
            for placeholder, value in url_params.items():
                url = url.replace(f':{str(placeholder)}', str(value))
        return url