import contextlib

import httpx

__all__ = ('closing_http_client_factory',)


@contextlib.asynccontextmanager
async def closing_http_client_factory(base_url: str) -> httpx.AsyncClient:
    async with httpx.AsyncClient(base_url=base_url) as client:
        yield client
