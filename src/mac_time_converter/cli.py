import click
from zoneinfo import ZoneInfo
from . import mac_time


@click.group()
def cli():
    pass


@cli.command()
@click.argument("timestamp", type=float)
@click.option("--timezone", "timezone_code")
def to_datetime(timestamp: float, timezone_code: str) -> None:
    timezone = ZoneInfo(timezone_code)
    dt = mac_time.to_datetime(timestamp).astimezone(timezone)
    click.echo(dt.strftime("%A %B %d, %Y at %H:%M:%S %Z"))
