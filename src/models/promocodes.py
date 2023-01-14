import datetime

from pydantic import BaseModel

__all__ = ('PromocodeActivated',)


class PromocodeActivated(BaseModel):
    subscription_expires_at: datetime.datetime
