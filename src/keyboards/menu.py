from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

__all__ = ('MenuMarkup',)


class MenuMarkup(ReplyKeyboardMarkup):

    def __init__(self):
        super().__init__(
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton('💳 Подписка'), KeyboardButton('❓ FAQ')],
                [KeyboardButton('👥 Поддержка'), KeyboardButton('🌐 Наш канал')],
            ],
        )
