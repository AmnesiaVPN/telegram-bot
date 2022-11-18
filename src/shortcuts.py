from aiogram.types import Message

from views.base import BaseView

__all__ = (
    'answer_view',
)


async def answer_view(message: Message, *views: BaseView, disable_web_page_preview: bool | None = None):
    for view in views:
        await message.answer(
            text=view.get_text(),
            reply_markup=view.get_reply_markup(),
            disable_web_page_preview=disable_web_page_preview,
        )
