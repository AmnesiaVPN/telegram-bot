from aiogram.dispatcher.filters.state import StatesGroup, State

__all__ = ('UserRegistrationStates',)


class UserRegistrationStates(StatesGroup):
    promocode = State()
