from aiogram.types import InlineKeyboardButton

from keyboards import PaymentMenuMarkup


def test_payment_menu_markup():
    url = 'https://google.com'
    expected_keyboard = [[InlineKeyboardButton('Продлить подписку', url=url)]]
    assert PaymentMenuMarkup(payment_page_url=url).inline_keyboard == expected_keyboard
