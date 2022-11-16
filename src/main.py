import pathlib

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode

import handlers
from config import load_config
from middlewares import ServerAPIMiddleware, ConfigMiddleware


async def on_startup(dispatcher: Dispatcher):
    handlers.menu.register_handlers(dispatcher)
    handlers.subscription.register_handlers(dispatcher)


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.ini'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot)

    config_middleware = ConfigMiddleware(config)
    server_api_middleware = ServerAPIMiddleware(config.server_api.base_url)

    dp.setup_middleware(config_middleware)
    dp.setup_middleware(server_api_middleware)

    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    main()
