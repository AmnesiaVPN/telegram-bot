from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message

from shortcuts import answer_view
from views import MenuView, FAQView

__all__ = ('register_handlers',)


async def on_user_start(message: Message):
    await answer_view(message, MenuView())


async def on_show_faq(message: Message):
    await answer_view(message, FAQView())


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_show_faq, Text('❓ FAQ'))
