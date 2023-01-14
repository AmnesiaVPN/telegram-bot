from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

__all__ = ('MenuMarkup',)


class MenuMarkup(ReplyKeyboardMarkup):

    def __init__(self, has_user_activated_promocode: bool):
        super().__init__(
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton('💳 Подписка'), KeyboardButton('❓ FAQ')],
                [KeyboardButton('👥 Поддержка'), KeyboardButton('🌐 Наш канал')],
            ],
        )
        if not has_user_activated_promocode:
            self.add(KeyboardButton('🏷️ Активировать промокод'))
