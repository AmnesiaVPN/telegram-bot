from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from services.server_api import ServerAPIClient

__all__ = ('ServerAPIMiddleware',)


class ServerAPIMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, api_base_url: str):
        super().__init__()
        self.__api_base_url = api_base_url

    async def pre_process(self, obj, data, *args):
        data["server_api_client"] = ServerAPIClient(self.__api_base_url)

    async def post_process(self, obj, data, *args):
        server_api_client: ServerAPIClient = data["server_api_client"]
        await server_api_client.close()
