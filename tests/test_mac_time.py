import src.mac_time_converter.mac_time as mac_time


def test_mac_to_datetime_at_epoch() -> None:
    assert mac_time.to_datetime(0) == mac_time.EPOCH


def test_datetime_to_mac_at_epoch() -> None:
    assert mac_time.from_datetime(mac_time.EPOCH) == 0
