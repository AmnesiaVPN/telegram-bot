from typing import Protocol

__all__ = ('MessageProtocol',)


class MessageProtocol(Protocol):
    """aiogram.types.Message's signature protocol"""

    text: str | None
