from aiogram.types import ReplyKeyboardMarkup

from views.base import BaseView
from keyboards import MenuMarkup

__all__ = ('InstructionView',)


class InstructionView(BaseView):
    text = '''<a href="https://telegra.ph/Instrukciya-po-ustanovke-VoblaVpn-11-18">ИНСТРУКЦИЯ ПО УСТАНОВКЕ.</a>'''

    def __init__(self, has_user_activated_promocode: bool):
        self.__has_user_activated_promocode = has_user_activated_promocode

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        return MenuMarkup(self.__has_user_activated_promocode)
