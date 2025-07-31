import pytest
from src.mac_time_converter.cli import cli
from click.testing import CliRunner, Result


@pytest.fixture(name="to_datetime_on_epoch_result")
def get_to_datetime_on_epoch_result() -> Result:
    return CliRunner().invoke(cli, ["to-datetime", "0", "--timezone", "UTC"])


@pytest.fixture(name="to_datetime_on_invalid_timezone_result")
def get_to_datetime_on_invalid_timezone_result() -> Result:
    return CliRunner().invoke(cli, ["to-datetime", "0", "--timezone", "BAD"])


@pytest.fixture(name="from_datetime_epoch_result")
def get_from_datetime_epoch_result() -> Result:
    return CliRunner().invoke(cli, ["from-datetime", "Janurary 1 1904"])


def test_epoch_utc_exits_without_error(to_datetime_on_epoch_result) -> None:
    assert to_datetime_on_epoch_result.exit_code == 0


def test_epoch_utc_has_year_in_output(to_datetime_on_epoch_result) -> None:
    assert "1904" in to_datetime_on_epoch_result.output


def test_epoch_utc_has_time_in_output(to_datetime_on_epoch_result) -> None:
    assert "00:00:00" in to_datetime_on_epoch_result.output


def test_epoch_utc_has_utc_in_output(to_datetime_on_epoch_result) -> None:
    assert "UTC" in to_datetime_on_epoch_result.output


def test_utc_is_not_the_timezone_when_no_timezone_is_passed() -> None:
    result = CliRunner().invoke(cli, ["to-datetime", "0"])
    assert "UTC" not in result.output


def test_invalid_timezone_exit_code(to_datetime_on_invalid_timezone_result) -> None:
    assert to_datetime_on_invalid_timezone_result.exit_code != 0


def test_invalid_timezone_has_error_output(to_datetime_on_invalid_timezone_result) -> None:
    assert "Error" in to_datetime_on_invalid_timezone_result.output


def test_from_datetime_does_not_default_to_utc(from_datetime_epoch_result) -> None:
    assert "UTC" not in from_datetime_epoch_result.output
