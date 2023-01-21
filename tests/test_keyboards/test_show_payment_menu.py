from aiogram.types import InlineKeyboardButton

from keyboards import ShowPaymentMenuMarkup


def test_show_payment_menu_markup():
    expected_keyboard = [[InlineKeyboardButton('Продлить подписку', callback_data='show-payment-menu')]]
    assert ShowPaymentMenuMarkup() == expected_keyboard
