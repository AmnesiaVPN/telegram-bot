from views.base import BaseView
from keyboards import MenuMarkup

__all__ = ('InstructionView',)


class InstructionView(BaseView):
    text = '''<a href="https://telegra.ph/Instrukciya-po-ustanovke-VoblaVpn-11-18">ИНСТРУКЦИЯ ПО УСТАНОВКЕ.</a>'''
    reply_markup = MenuMarkup()
