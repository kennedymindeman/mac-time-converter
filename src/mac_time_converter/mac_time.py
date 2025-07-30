from datetime import datetime, timedelta
from dataclasses import dataclass


class MacTime:
    EPOCH = datetime(
        year=1904,
        month=1,
        day=1,
    )

def to_datetime(cls, seconds: float) -> datetime:
    return EPOCH + timedelta(seconds=seconds)

def from_data