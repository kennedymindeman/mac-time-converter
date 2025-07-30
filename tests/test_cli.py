from src.mac_time_converter.cli import cli
from click.testing import CliRunner


def test_epoch_utc_output() -> None:
    result = CliRunner().invoke(cli, ["to-datetime", "0", "--timezone", "UTC"])
    assert result.exit_code == 0
