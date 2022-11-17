from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from shortcuts import answer_view
from views import FAQView, NewsChannelView, SupportView

__all__ = ('register_handlers',)


async def on_show_faq(message: Message):
    await answer_view(message, FAQView())


async def on_show_news_channel(message: Message):
    await answer_view(message, NewsChannelView())


async def on_show_support_bot(message: Message):
    await answer_view(message, SupportView())


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_show_faq, Text('❓ FAQ'))
    dispatcher.register_message_handler(on_show_news_channel, Text('🌐 Наш канал'))
    dispatcher.register_message_handler(on_show_support_bot, Text('👥 Поддержка'))
