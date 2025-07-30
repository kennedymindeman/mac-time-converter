from datetime import datetime, timedelta


EPOCH = datetime(
    year=1904,
    month=1,
    day=1,
)

def to_datetime(seconds: float) -> datetime:
    return EPOCH + timedelta(seconds=seconds)
