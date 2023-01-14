import datetime

from aiogram.types import ReplyKeyboardMarkup

from keyboards import MenuMarkup
from views.base import BaseView

__all__ = ('PromocodeActivatedView',)


class PromocodeActivatedView(BaseView):

    def __init__(self, *, subscription_expires_at: datetime.datetime):
        self.__subscription_expires_at = subscription_expires_at

    def get_text(self) -> str:
        subscription_expires_at = self.__subscription_expires_at + datetime.timedelta(hours=3)
        return (
            '✅ Ваша подписка продлена до'
            f' {subscription_expires_at:%d.%m.%Y %H:%M:%S}'
        )

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        return MenuMarkup(has_user_activated_promocode=True)
