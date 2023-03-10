from aiogram.types import InlineKeyboardMarkup

from keyboards import PaymentMenuMarkup
from views.base import BaseView

__all__ = ('PaymentMenuView',)


class PaymentMenuView(BaseView):
    __slots__ = ('__telegram_id', '__payment_page_url',)

    def __init__(self, telegram_id: int, payment_page_url: str):
        self.__telegram_id = telegram_id
        self.__payment_page_url = payment_page_url

    def get_text(self) -> str:
        return (
            'Оплата подписки производится через систему donationalerts. Стоимость продления 299 рублей.'
            '\n\n❗️ <b>Важно</b> ❗️'
            f'\nВ примечаниях к платежу, обязательно, введите "<b>{self.__telegram_id}</b>"'
            f' , иначе ваша оплата не будет засчитана'
        )

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        return PaymentMenuMarkup(self.__payment_page_url)
