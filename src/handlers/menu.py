from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message

from shortcuts import answer_view
from views import MenuView, FAQView, NewsChannelView

__all__ = ('register_handlers',)


async def on_user_start(message: Message):
    await answer_view(message, MenuView())


async def on_show_faq(message: Message):
    await answer_view(message, FAQView())


async def on_show_news_channel(message: Message):
    await answer_view(message, NewsChannelView())


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_show_faq, Text('❓ FAQ'))
    dispatcher.register_message_handler(on_show_news_channel, Text('🌐 Наш канал'))
