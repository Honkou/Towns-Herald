"""File containing all unit tests for server_time.py file."""

from datetime import datetime, tzinfo

import pytest
from pytz import timezone, utc
from server_time import TimesOfDay, get_servers_local_timezone, get_time_of_day, utc_to_local_time


@pytest.mark.parametrize(
    ("test_hour", "expected_time_of_day"),
    [
        (3, TimesOfDay.NIGHT),
        (6, TimesOfDay.MORNING),
        (9, TimesOfDay.MORNING),
        (13, TimesOfDay.AFTERNOON),
        (18, TimesOfDay.EVENING),
        (23, TimesOfDay.NIGHT),
    ],
)
def test_get_time_of_day(test_hour: int, expected_time_of_day: TimesOfDay):
    """Assert that get_time_of_day returns expected Enum."""
    testing_time = datetime(year=2023, month=6, day=8, hour=test_hour, tzinfo=utc)
    assert get_time_of_day(testing_time) == expected_time_of_day


def test_get_servers_local_timezone():
    """Assert that the function returns expected object type."""
    server_timezone = get_servers_local_timezone()
    assert isinstance(server_timezone, tzinfo)


@pytest.mark.parametrize(
    ("month", "expected_offset"),
    [(6, 2), (11, 1)],
)
def test_utc_to_local_time(month, expected_offset):
    """Assert that the function converts utc date to the same date in a different timezone.

    This tests June and November separately to make sure that daylight savings are correctly applied.
    """
    testing_date = datetime(year=2023, month=month, day=8, hour=11, tzinfo=utc)
    new_timezone = timezone("Europe/Warsaw")

    new_date = utc_to_local_time(testing_date, new_timezone)
    hour_offset = new_date.hour - testing_date.hour
    assert hour_offset == expected_offset
