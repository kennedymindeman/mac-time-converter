from datetime import datetime, timedelta
from dataclasses import dataclass


class MacTime:
    EPOCH = datetime(
        year=1904,
        month=1,
        day=1,
    )

    @classmethod
    def to_datetime(cls, seconds: float) -> datetime:
        return MacTime.EPOCH + timedelta(seconds=seconds)
