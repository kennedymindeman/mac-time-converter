from datetime import datetime, timedelta, timezone
import src.mac_time_converter.mac_time as mac_time


def test_mac_to_datetime_at_epoch() -> None:
    assert mac_time.to_datetime(0) == mac_time.EPOCH


def test_datetime_to_mac_at_epoch() -> None:
    assert mac_time.from_datetime(mac_time.EPOCH) == 0


def test_one_second_after_epoch() -> None:
    assert mac_time.from_datetime(mac_time.EPOCH + timedelta(seconds=1)) == 1


def test_round_trip() -> None:
    dt = datetime(
        year=2022,
        month=2,
        day=2,
        tzinfo=timezone.utc,
    )
    assert mac_time.to_datetime(mac_time.from_datetime(dt)) == dt
