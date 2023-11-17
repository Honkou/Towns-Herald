"""File containing all unit tests for server_time.py file."""

from datetime import datetime

import pytest
from pytz import utc
from server_time import TimesOfDay, get_time_of_day


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
