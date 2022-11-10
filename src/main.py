import pathlib

from aiogram import Bot, Dispatcher, executor

import handlers
from config import load_config


async def on_startup(dispatcher: Dispatcher):
    handlers.menu.register_handlers(dispatcher)


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.ini'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token)
    dp = Dispatcher(bot)
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    main()
