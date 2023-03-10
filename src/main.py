import pathlib
import functools

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

import handlers
from config import load_config
from middlewares import DependencyInjectMiddleware
from services.users import UsersAPIService
from services.http_client import closing_http_client_factory


async def on_startup(dispatcher: Dispatcher):
    handlers.menu.register_handlers(dispatcher)
    handlers.subscription.register_handlers(dispatcher)
    handlers.promocodes.register_handlers(dispatcher)


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.toml'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    configured_http_client_factory = functools.partial(
        closing_http_client_factory,
        base_url=config.server_api.base_url,
    )
    users_api_service = UsersAPIService(configured_http_client_factory)

    dependency_inject_middleware = DependencyInjectMiddleware(
        users_api_service=users_api_service,
        config=config,
    )
    dp.setup_middleware(dependency_inject_middleware)

    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    main()
