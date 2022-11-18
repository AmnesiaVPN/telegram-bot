import datetime

import models
from views.base import BaseView

from keyboards import MenuMarkup

__all__ = ('MenuView',)


class MenuView(BaseView):
    reply_markup = MenuMarkup()

    def __init__(self, user: models.User):
        self.__user = user

    def get_text(self) -> str:
        lines = []
        if not self.__user.is_subscribed:
            return '❗️ У вас нет активной подписки'
        if self.__user.is_trial_period:
            lines.append('❗️ У вас пробный период')

        subscribed_at = self.__user.subscribed_at + datetime.timedelta(hours=3)
        subscription_expire_at = self.__user.subscription_expire_at + datetime.timedelta(hours=3)
        lines.append(
            f'Подписка активирована: {subscribed_at:%H:%M %d.%m.%Y}'
            f'\nАктивна до: {subscription_expire_at:%H:%M %d.%m.%Y}'
        )
        return '\n'.join(lines)
