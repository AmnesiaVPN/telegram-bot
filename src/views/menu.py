import models
from views.base import BaseView

from keyboards import MenuMarkup
from services.subscription import is_subscription_active

__all__ = ('MenuView',)


class MenuView(BaseView):
    reply_markup = MenuMarkup()

    def __init__(self, user: models.User):
        self.__user = user

    def get_text(self) -> str:
        lines = []
        if not is_subscription_active(self.__user.subscribed_at, self.__user.subscription_expire_at):
            return '❗️ У вас нету активной подписки'
        if self.__user.is_trial_period:
            lines.append('❗️ У вас пробный период')
        lines.append(
            f'Подписка активирована: {self.__user.subscribed_at:%H:%M %d.%m.%Y}'
            f'\nАктивна до: {self.__user.subscription_expire_at:%H:%M %d.%m.%Y}'
        )
        return '\n'.join(lines)
