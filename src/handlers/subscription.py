from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, CallbackQuery

import exceptions
import models
from config import Config
from states import UserRegistrationStates
from repositories import UserRepository
from services.temp_files import deleting_temporary_config_file
from shortcuts import answer_view
from views import MenuView, PaymentMenuView, InstructionView, PromocodeView

__all__ = ('register_handlers',)


async def on_user_registered(message: Message, user: models.User, config: Config, user_repository: UserRepository):
    await answer_view(message, MenuView(user, config.donationalerts.payment_page_url))
    if not user.is_subscribed:
        await answer_view(message, PaymentMenuView(message.from_user.id, config.donationalerts.payment_page_url))
        return
    user_config_text = await user_repository.get_config(message.from_user.id)
    await answer_view(message, InstructionView(), disable_web_page_preview=True)
    with deleting_temporary_config_file(message.from_user.id, user_config_text) as user_config:
        await message.answer_document(user_config)


async def on_show_payment_menu(callback_query: CallbackQuery, config: Config):
    view = PaymentMenuView(callback_query.from_user.id, config.donationalerts.payment_page_url)
    await answer_view(callback_query.message, view)
    await callback_query.answer()


async def on_user_has_no_promocode(
        message: Message,
        user_repository: UserRepository,
        config: Config,
        state: FSMContext,
):
    user = await user_repository.create(message.from_user.id)
    await state.finish()
    await on_user_registered(message, user, config, user_repository)


async def on_promocode_input(
        message: Message,
        user_repository: UserRepository,
        config: Config,
        state: FSMContext,
):
    user = await user_repository.create(message.from_user.id)
    await state.finish()
    await on_user_registered(message, user, config, user_repository)


async def on_user_not_registered(message: Message):
    await UserRegistrationStates.promocode.set()
    await answer_view(message, PromocodeView())


async def on_user_start(message: Message, user_repository: UserRepository, config: Config):
    try:
        user = await user_repository.get_by_telegram_id(message.from_user.id)
    except exceptions.UserNotFoundError:
        await on_user_not_registered(message)
    else:
        await on_user_registered(message, user, config, user_repository)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        on_user_has_no_promocode,
        Text('У меня нет промокода'),
        state=UserRegistrationStates.promocode,
    )
    dispatcher.register_message_handler(
        on_promocode_input,
        state=UserRegistrationStates.promocode,
    )
    dispatcher.register_callback_query_handler(on_show_payment_menu, Text('show-payment-menu'))
    dispatcher.register_message_handler(on_user_start, CommandStart())
    dispatcher.register_message_handler(on_user_start, Text('💳 Подписка'))
