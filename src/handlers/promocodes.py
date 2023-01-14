from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, Update, ContentType

from core import exceptions
from filters import MessageLengthFilter
from services.users import UsersAPIService
from shortcuts import answer_view
from states import ActivatePromocodeStates
from views import PromocodeActivatedView


async def on_promocode_not_found_error(
        update: Update,
        exception: exceptions.PromocodeNotFoundError,
) -> bool:
    await update.message.answer('❌ Промокод не найден')
    return True


async def on_user_already_activated_promocode_error(
        update: Update,
        exception: exceptions.UserAlreadyActivatedPromocodeError,
) -> bool:
    await update.message.answer('🙅‍♂️ Вы уже активировали промокод')
    return True


async def on_promocode_input_invalid_length(message: Message) -> None:
    await message.answer('❗️ Неправильный формат промокода')


async def on_promocode_input(message: Message, users_api_service: UsersAPIService, state: FSMContext) -> None:
    promocode_activated = await users_api_service.activate_promocode(message.from_user.id, message.text)
    await state.finish()
    view = PromocodeActivatedView(subscription_expires_at=promocode_activated.subscription_expires_at)
    await answer_view(message, view)


async def on_activate_promocode_menu(message: Message, users_api_service: UsersAPIService) -> None:
    user = await users_api_service.get_by_telegram_id(message.from_user.id)
    if user.has_activated_promocode:
        raise exceptions.UserAlreadyActivatedPromocodeError
    await ActivatePromocodeStates.promocode.set()
    await message.answer('📲 Введите ваш промокод')


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_errors_handler(
        on_promocode_not_found_error,
        exception=exceptions.PromocodeNotFoundError,
    )
    dispatcher.register_errors_handler(
        on_user_already_activated_promocode_error,
        exception=exceptions.UserAlreadyActivatedPromocodeError,
    )
    dispatcher.register_message_handler(
        on_promocode_input_invalid_length,
        ~MessageLengthFilter(min_length=8, max_length=8),
        content_types=ContentType.TEXT,
        state=ActivatePromocodeStates.promocode,
    )
    dispatcher.register_message_handler(
        on_promocode_input,
        content_types=ContentType.TEXT,
        state=ActivatePromocodeStates.promocode,
    )
    dispatcher.register_message_handler(
        on_activate_promocode_menu,
        Text('🏷️ Активировать промокод'),
        state='*',
    )
