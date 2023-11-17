"""Utility module responsible for processing requests related to time."""

from datetime import datetime
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
