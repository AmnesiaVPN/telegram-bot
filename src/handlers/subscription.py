from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, CallbackQuery

import models
from config import Config
from core import exceptions
from services.temp_files import deleting_temporary_config_file
from services.users import UsersAPIService
from shortcuts import answer_view
from views import MenuView, PaymentMenuView, InstructionView

__all__ = ('register_handlers',)


async def on_user_registered(message: Message, user: models.User, config: Config, users_api_service: UsersAPIService):
    await answer_view(message, MenuView(user, config.donationalerts.payment_page_url))
    if not user.is_subscribed:
        await answer_view(message, PaymentMenuView(message.from_user.id, config.donationalerts.payment_page_url))
        return
    user_config_text = await users_api_service.get_config(message.from_user.id)
    await answer_view(message, InstructionView(user.has_activated_promocode), disable_web_page_preview=True)
    with deleting_temporary_config_file(message.from_user.id, user_config_text) as user_config:
        await message.answer_document(user_config)


async def on_show_payment_menu(callback_query: CallbackQuery, config: Config):
    view = PaymentMenuView(callback_query.from_user.id, config.donationalerts.payment_page_url)
    await answer_view(callback_query.message, view)
    await callback_query.answer()


async def on_user_start(message: Message, users_api_service: UsersAPIService, config: Config, state: FSMContext):
    try:
        user = await users_api_service.get_by_telegram_id(message.from_user.id)
    except exceptions.UserNotFoundError:
        user = await users_api_service.create(message.from_user.id)
    await on_user_registered(message, user, config, users_api_service)
    await state.finish()


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(
        on_show_payment_menu,
        Text('show-payment-menu'),
        state='*',
    )
    dispatcher.register_message_handler(
        on_user_start,
        CommandStart() | Text('💳 Подписка'),
        state='*',
    )
