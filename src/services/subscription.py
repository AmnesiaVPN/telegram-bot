import datetime


def is_subscription_active(starts_at: datetime.datetime, ends_at: datetime.datetime) -> bool:
    starts_at = starts_at.replace(tzinfo=None)
    ends_at = ends_at.replace(tzinfo=None)
    return starts_at <= datetime.datetime.utcnow() <= ends_at
