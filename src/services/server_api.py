import contextlib

import httpx

import exceptions
import models
from config import ROOT_PATH


class ServerAPIClient:

    def __init__(self, base_url: str):
        self.__base_url = base_url
        self.__http_client = httpx.AsyncClient(base_url=base_url)

    async def create_user(self, telegram_id: int) -> models.User:
        response = await self.__http_client.post('/users/', json={'telegram_id': telegram_id})
        if response.status_code == 200:
            return models.User.parse_obj(response.json())
        elif response.status_code == 409:
            raise exceptions.UserAlreadyExistsError

    async def get_user(self, telegram_id: int) -> models.User:
        response = await self.__http_client.get(f'/users/{telegram_id}/')
        if response.status_code == 200:
            return models.User.parse_obj(response.json())
        elif response.status_code == 404:
            raise exceptions.UserNotFoundError

    async def get_or_create_user(self, telegram_id: int) -> tuple[models.User, bool]:
        try:
            return await self.get_user(telegram_id), False
        except exceptions.UserNotFoundError:
            return await self.create_user(telegram_id), True

    async def get_user_config(self, telegram_id: int) -> str:
        response = await self.__http_client.get(f'/users/{telegram_id}/config/')
        if response.is_error:
            raise Exception
        return response.text

    async def close(self):
        await self.__http_client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


@contextlib.contextmanager
def deleting_temporary_config_file(telegram_id: int, config_file_text: str) -> bytes:
    file_path = ROOT_PATH / f'{telegram_id}.conf'
    try:
        file_path.write_text(config_file_text)
        with open(file_path, 'rb') as file:
            yield file
    finally:
        file_path.unlink(missing_ok=True)
