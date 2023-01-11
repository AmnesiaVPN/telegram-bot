from aiogram.dispatcher.filters.state import StatesGroup, State

__all__ = ('ActivatePromocodeStates',)


class ActivatePromocodeStates(StatesGroup):
    promocode = State()
