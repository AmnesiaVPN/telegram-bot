from typing import Callable

import httpx

import exceptions
import models

__all__ = ('UsersAPIService',)


class UsersAPIService:

    def __init__(self, http_client_factory: Callable[[], httpx.AsyncClient]):
        self.__http_client_factory = http_client_factory

    async def create(self, telegram_id: int) -> models.User:
        async with self.__http_client_factory() as client:
            response = await client.post('/users/', json={'telegram_id': telegram_id})
        if response.status_code == 200:
            return models.User.parse_obj(response.json())
        elif response.status_code == 409:
            raise exceptions.UserAlreadyExistsError

    async def get_by_telegram_id(self, telegram_id: int) -> models.User:
        url = f'/users/{telegram_id}/'
        async with self.__http_client_factory() as client:
            response = await client.get(url)
        if response.status_code == 200:
            return models.User.parse_obj(response.json())
        elif response.status_code == 404:
            raise exceptions.UserNotFoundError

    async def get_or_create(self, telegram_id: int) -> tuple[models.User, bool]:
        try:
            return await self.get_by_telegram_id(telegram_id), False
        except exceptions.UserNotFoundError:
            return await self.create(telegram_id), True

    async def get_config(self, telegram_id: int) -> str:
        url = f'/users/{telegram_id}/config/'
        async with self.__http_client_factory() as client:
            response = await client.get(url)
        if response.is_error:
            raise Exception
        return response.text

    async def activate_promocode(self, telegram_id: int, promocode: str) -> models.PromocodeActivated:
        url = f'/users/{telegram_id}/promocodes/'
        request_body = {'promocode': promocode}
        async with self.__http_client_factory() as client:
            response = await client.post(url, json=request_body)
        response_body = response.json()
        return models.PromocodeActivated.parse_obj(response_body)
