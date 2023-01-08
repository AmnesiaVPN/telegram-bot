from views.base import BaseView
from keyboards import PromocodeSkipMarkup

__all__ = ('PromocodeView',)


class PromocodeView(BaseView):
    text = 'Введите ваш промокод если он у вас есть'
    reply_markup = PromocodeSkipMarkup()
