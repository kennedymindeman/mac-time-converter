from datetime import datetime


def test_mac_to_datetime_at_epoch() -> None:
    assert MacTime.to_datetime(0) == datetime(
        year=1904,
        month=1,
        day=1,
    )
