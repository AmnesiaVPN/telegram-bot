from typing import Callable

import httpx

import models
from core import exceptions

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
        if response.status_code == 200:
            return models.PromocodeActivated.parse_obj(response_body)

        error_message = response_body['message']
        match [error_message, response.status_code]:
            case ['Promocode is not found', 404]:
                raise exceptions.PromocodeNotFoundError
            case ['Each user can activate only one promocode', 409]:
                raise exceptions.UserAlreadyActivatedPromocodeError
            case ['Promocode was already activated', 409]:
                raise exceptions.PromocodeWasActivatedError
            case ['Promocode was already expired', 410]:
                raise exceptions.PromocodeWasExpiredError
