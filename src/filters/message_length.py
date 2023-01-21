from aiogram.dispatcher.filters import BoundFilter

from models.protocols import MessageProtocol

__all__ = ('MessageLengthFilter',)


class MessageLengthFilter(BoundFilter):
    key = 'message_length'

    __slots__ = ('__max_length',)

    def __init__(self, *, min_length: int | None = None, max_length: int | None = None):
        self.__min_length = min_length or 1
        self.__max_length = max_length or 4096

    async def check(self, message: MessageProtocol) -> bool:
        return self.__min_length <= len(message.text) <= self.__max_length
