from views.base import BaseView

from keyboards import MenuMarkup

__all__ = ('MenuView',)


class MenuView(BaseView):
    text = 'menu'
    reply_markup = MenuMarkup()
