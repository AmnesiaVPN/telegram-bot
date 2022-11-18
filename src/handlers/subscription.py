from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, CallbackQuery

from config import Config
from services.server_api import ServerAPIClient, deleting_temporary_config_file
from shortcuts import answer_view
from views import MenuView, PaymentMenuView, InstructionView

__all__ = ('register_handlers',)


async def on_show_payment_menu(callback_query: CallbackQuery, config: Config):
    view = PaymentMenuView(callback_query.from_user.id, config.donationalerts.payment_page_url)
    await answer_view(callback_query.message, view)
    await callback_query.answer()


async def on_user_start(message: Message, server_api_client: ServerAPIClient, config: Config):
    user, _ = await server_api_client.get_or_create_user(message.from_user.id)
    await answer_view(message, MenuView(user, config.donationalerts.payment_page_url))
    if not user.is_subscribed:
        await answer_view(message, PaymentMenuView(message.from_user.id, config.donationalerts.payment_page_url))
        return
    user_config_text = await server_api_client.get_user_config(message.from_user.id)
    await answer_view(message, InstructionView(), disable_web_page_preview=True)
    with deleting_temporary_config_file(message.from_user.id, user_config_text) as user_config:
        await message.answer_document(user_config)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(on_show_payment_menu, Text('show-payment-menu'))
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_user_start, Text('💳 Подписка'))
