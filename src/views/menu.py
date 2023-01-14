import datetime

from aiogram.types import InlineKeyboardMarkup

import models
from keyboards import ShowPaymentMenuMarkup
from views.base import BaseView

__all__ = ('MenuView',)


class MenuView(BaseView):

    def __init__(self, user: models.User, payment_page_url: str):
        self.__user = user
        self.__payment_page_url = payment_page_url

    def get_text(self) -> str:
        lines = []
        if not self.__user.is_subscribed:
            return '❗️ У вас нет активной подписки'
        if self.__user.is_trial_period:
            lines.append('❗️ У вас пробный период')

        subscribed_at = self.__user.subscribed_at + datetime.timedelta(hours=3)
        subscription_expire_at = self.__user.subscription_expires_at + datetime.timedelta(hours=3)
        lines.append(
            f'Подписка активирована: {subscribed_at:%H:%M %d.%m.%Y}'
            f'\nАктивна до: {subscription_expire_at:%H:%M %d.%m.%Y}'
        )
        return '\n'.join(lines)

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        if self.__user.is_subscribed:
            return ShowPaymentMenuMarkup()
