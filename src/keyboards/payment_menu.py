from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = ('PaymentMenuMarkup',)


class PaymentMenuMarkup(InlineKeyboardMarkup):

    def __init__(self, payment_page_url: str):
        super().__init__(row_width=1)
        self.add(InlineKeyboardButton('Продлить подписку', url=payment_page_url))
