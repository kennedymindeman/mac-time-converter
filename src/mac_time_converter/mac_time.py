from datetime import datetime, timedelta, timezone


EPOCH = datetime(
    year=1904,
    month=1,
    day=1,
    tzinfo=timezone.utc,
)
"""Mac time epoch: January 1, 1904 00:00:00 UTC.

This is the reference point for Mac/HFS+ timestamp calculations.
"""


def to_datetime(seconds: float) -> datetime:
    """Convert Mac timestamp to datetime object.

    Args:
        seconds: Number of seconds since Mac epoch (January 1, 1904).
                Can be negative for dates before the epoch.

    Returns:
        datetime object representing the timestamp.

    Example:
        >>> to_datetime(0)
        datetime.datetime(1904, 1, 1, 0, 0)
        >>> to_datetime(86400)  # One day later
        datetime.datetime(1904, 1, 2, 0, 0)
    """
    return EPOCH + timedelta(seconds=seconds)


def from_datetime(dt: datetime) -> float:
    """Convert datetime object to Mac timestamp.

    Args:
        dt: datetime object to convert. Must be timezone-aware.

    Returns:
        Number of seconds since Mac epoch (January 1, 1904 UTC).
        Negative values indicate dates before the epoch.

    Examples:
        >>> from_datetime(datetime(1904, 1, 1, tzinfo=timezone.utc))
        0.0
        >>> from_datetime(datetime(1904, 1, 2, tzinfo=timezone.utc))
        86400.0
    """
    return (dt - EPOCH).total_seconds()
