import click
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from . import mac_time


@click.group()
def cli():
    pass


@cli.command()
@click.argument("timestamp", type=float)
@click.option("--timezone", "timezone_code")
def to_datetime(timestamp: float, timezone_code: str) -> None:
    try:
        timezone = get_timezone(timezone_code)
    except ZoneInfoNotFoundError:
        click.echo(f"Error: Unknown timezone '{timezone_code}'", err=True)
        click.echo("Try 'UTC', 'US/Eastern', 'Europe/London', etc.", err=True)
        raise click.Abort()
    else:
        dt = mac_time.to_datetime(timestamp).astimezone(timezone)
        click.echo(dt.strftime("%A %B %d, %Y at %H:%M:%S %Z"))


def get_timezone(timezone_code: str) -> ZoneInfo | None:
    if not timezone_code:
        return None
    return ZoneInfo(timezone_code)
