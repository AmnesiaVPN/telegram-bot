from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

__all__ = ('PromocodeSkipMarkup',)


class PromocodeSkipMarkup(ReplyKeyboardMarkup):

    def __init__(self):
        super().__init__(
            resize_keyboard=True,
            keyboard=[[KeyboardButton('У меня нет промокода')]],
        )
