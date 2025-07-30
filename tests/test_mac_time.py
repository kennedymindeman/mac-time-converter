from datetime import datetime
from src.mac_time_converter.mac_time import MacTime


def test_mac_to_datetime_at_epoch() -> None:
    assert MacTime.to_datetime(0) == datetime(
        year=1904,
        month=1,
        day=1,
    )
