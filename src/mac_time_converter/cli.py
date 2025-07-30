import click
from datetime import datetime
from zoneinfo import ZoneInfo
from . import mac_time


@click.group()
def cli():
    pass


@cli.command()
@click.argument("timestamp", type=float)
@click.option("--timezone", "timezone_code")
def to_datetime(timestamp: float, timezone_code: str) -> None:
    if timezone_code:
        timezone = ZoneInfo(timezone_code)
    else:
        timezone = datetime.now().astimezone().tzinfo
    dt = mac_time.to_datetime(timestamp).astimezone(timezone)
    click.echo(dt.strftime("%A %B %d, %Y at %H:%M:%S %Z"))
