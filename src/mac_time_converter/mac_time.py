from datetime import datetime, timedelta, timezone


EPOCH = datetime(
    year=1904,
    month=1,
    day=1,
    tzinfo=timezone.utc,
)


def to_datetime(seconds: float) -> datetime:
    return EPOCH + timedelta(seconds=seconds)


def from_datetime(dt: datetime) -> float:
    return (dt - EPOCH).total_seconds()
