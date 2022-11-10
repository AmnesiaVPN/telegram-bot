from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from shortcuts import answer_view
from views import MenuView

__all__ = ('register_handlers',)


async def on_user_start(message: Message):
    await answer_view(message, MenuView())


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_user_start, CommandStart())
