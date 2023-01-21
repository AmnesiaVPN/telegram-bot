import pytest
from aiogram.types import KeyboardButton

from keyboards import MenuMarkup


@pytest.fixture
def menu_keyboard():
    return [
        [KeyboardButton('💳 Подписка'), KeyboardButton('❓ FAQ')],
        [KeyboardButton('👥 Поддержка'), KeyboardButton('🌐 Наш канал')],
    ]


def test_menu_keyboard(menu_keyboard):
    assert MenuMarkup(has_user_activated_promocode=True).keyboard == menu_keyboard
    menu_keyboard_with_promocode_button = menu_keyboard + [[KeyboardButton('🏷️ Активировать промокод')]]
    assert MenuMarkup(has_user_activated_promocode=False).keyboard == menu_keyboard_with_promocode_button
