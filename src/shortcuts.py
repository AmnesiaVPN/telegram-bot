import asyncio

from aiogram.types import Message

from views.base import BaseView

__all__ = (
    'answer_view',
    'sleep_for',
)


async def sleep_for(*, seconds: int | float) -> None:
    """Prevent brute force by slowing down promocode activation process."""
    await asyncio.sleep(seconds)


async def answer_view(message: Message, *views: BaseView, disable_web_page_preview: bool | None = None):
    for view in views:
        await message.answer(
            text=view.get_text(),
            reply_markup=view.get_reply_markup(),
            disable_web_page_preview=disable_web_page_preview,
        )
