import datetime

from pydantic import BaseModel

__all__ = ('User',)


class User(BaseModel):
    telegram_id: int
    subscription_expires_at: datetime.datetime
    subscribed_at: datetime.datetime
    is_trial_period: bool
    is_subscribed: bool
    has_activated_promocode: bool
