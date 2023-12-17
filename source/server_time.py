"""Utility module responsible for processing requests related to time."""

from datetime import datetime, tzinfo
from enum import IntEnum


class TimesOfDay(IntEnum):
    """Defines all possible parts of day, along with hours at which they begin."""

    MORNING = 6
    AFTERNOON = 12
    EVENING = 18
    NIGHT = 22


def get_time_of_day(date: datetime) -> TimesOfDay:
    """Return the time of day that's matching the time in the provided date."""
    hour = date.hour
    last_matching_day_part = TimesOfDay.NIGHT

    for day_part in TimesOfDay:
        if hour >= day_part.value:
            last_matching_day_part = day_part
    return last_matching_day_part


def get_servers_local_timezone() -> tzinfo:
    """Return information of the server's timezone, on which the bot is hosted."""
    local_timezone = datetime.now().astimezone().tzinfo
    if not local_timezone:
        msg = "Expected timezone object, but no timezone was returned!"
        raise ValueError(msg)
    return local_timezone


def utc_to_local_time(date: datetime, tz: tzinfo) -> datetime:
    """Convert a UTC time to match a timezone.

    This is needed in order to operate on the bot's local time, instead of the universal one.
    """
    return date.astimezone(tz=tz)
