from typing import Callable

import httpx

__all__ = ('Repository',)


class Repository:
    __slots__ = ('_http_client_factory',)

    def __init__(self, http_client_factory: Callable[[], httpx.AsyncClient]):
        self._http_client_factory = http_client_factory
