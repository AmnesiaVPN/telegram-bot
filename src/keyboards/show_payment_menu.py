from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = ('ShowPaymentMenuMarkup',)


class ShowPaymentMenuMarkup(InlineKeyboardMarkup):

    def __init__(self):
        super().__init__()
        self.add(
            InlineKeyboardButton('Продлить подписку', callback_data='show-payment-menu')
        )
