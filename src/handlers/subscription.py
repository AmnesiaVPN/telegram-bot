from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message

from services.server_api import ServerAPIClient, deleting_temporary_config_file
from shortcuts import answer_view
from views import MenuView

__all__ = ('register_handlers',)


async def on_user_start(message: Message, server_api_client: ServerAPIClient):
    user, _ = await server_api_client.get_or_create_user(message.from_user.id)
    await answer_view(message, MenuView(user))
    if not user.is_subscribed:
        return
    user_config_text = await server_api_client.get_user_config(message.from_user.id)
    with deleting_temporary_config_file(message.from_user.id, user_config_text) as user_config:
        await message.answer_document(user_config)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_user_start, Text('💳 Подписка'))
