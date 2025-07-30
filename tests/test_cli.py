import pytest
from src.mac_time_converter.cli import cli
from click.testing import CliRunner, Result


@pytest.fixture(name="to_datetime_on_epoch_result")
def get_to_datetime_on_epoch_result() -> Result:
    return CliRunner().invoke(cli, ["to-datetime", "0", "--timezone", "UTC"])


def test_epoch_utc_exits_without_error(to_datetime_on_epoch_result) -> None:
    assert to_datetime_on_epoch_result.exit_code == 0
