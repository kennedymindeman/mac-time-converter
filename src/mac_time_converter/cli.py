import click
from . import mac_time


@click.group()
def cli():
    pass


@cli.command()
@click.argument("timestamp", type=float)
@click.option("--timezone", "timezone_code")
def to_datetime(timestamp: float, timezone_code: str) -> None:
    click.echo(mac_time.to_datetime(timestamp))
