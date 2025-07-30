import pytest
from src.mac_time_converter.cli import cli
from click.testing import CliRunner, Result


@pytest.fixture(name="to_datetime_on_epoch_result")
def get_to_datetime_on_epoch_result() -> Result:
    return CliRunner().invoke(cli, ["to-datetime", "0", "--timezone", "UTC"])


def test_epoch_utc_exits_without_error(to_datetime_on_epoch_result) -> None:
    assert to_datetime_on_epoch_result.exit_code == 0


def test_epoch_utc_has_date_in_output(to_datetime_on_epoch_result) -> None:
    assert "1904-01-01" in to_datetime_on_epoch_result.output


def test_epoch_utc_has_time_in_output(to_datetime_on_epoch_result) -> None:
    assert "00:00:00" in to_datetime_on_epoch_result.output
