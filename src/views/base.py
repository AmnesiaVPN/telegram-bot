from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ForceReply, ReplyKeyboardRemove

__all__ = (
    'ReplyMarkup',
    'BaseView',
)

ReplyMarkup = InlineKeyboardMarkup | ReplyKeyboardMarkup | ForceReply | ReplyKeyboardRemove


class BaseView:
    text: str | None = None
    reply_markup: ReplyMarkup | None = None

    def get_text(self) -> str | None:
        return self.text

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup
