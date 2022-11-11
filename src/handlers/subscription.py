from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message

from services.server_api import ServerAPIClient
from shortcuts import answer_view
from views import InstructionView, MenuView

__all__ = ('register_handlers',)


async def on_user_start(message: Message, server_api_client: ServerAPIClient):
    user, is_created = await server_api_client.get_or_create_user(message.from_user.id)
    if is_created:
        await answer_view(message, InstructionView())
    await answer_view(message, MenuView(user))


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_user_start, Text('💳 Подписка'))
