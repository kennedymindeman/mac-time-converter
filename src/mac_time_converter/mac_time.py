from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass(frozen=True)
class MacTime:
    epoch = datetime(
        year=1904,
        month=1,
        day=1,
    )

    @staticmethod
    def to_datetime(seconds: float) -> datetime:
        return MacTime.epoch + timedelta(seconds=seconds)
