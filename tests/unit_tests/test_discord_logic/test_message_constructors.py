"""Test constructors creating expected response based on received context."""
from enum import Enum

import pytest
from discord_logic.message_constructors import (
    _get_time_based_greeting,
    create_hello_response_based_on_time,
)
from server_time import TimesOfDay


class TestHelloBasedOnTime:
    """Test suite for 'create_hello_response_based_on_time()' function."""

    def test_returns_string(self):
        """Assert the function returns a string."""
        response = create_hello_response_based_on_time()
        assert isinstance(response, str)

    @pytest.mark.parametrize(
        "user",
        ["Honkou", "Rysia", "Terminator"],
    )
    def test_addresses_user(self, user):
        """Assert the function mentions the user in response."""
        response = create_hello_response_based_on_time(user)
        assert response == f"Cześć, <@{user}>!"

    def test_skips_user_if_not_provided(self):
        """Assert the function skips the user if they were not mentioned."""
        response = create_hello_response_based_on_time()
        assert response == "Cześć!"

    def test_skips_user_if_string_is_empty(self):
        """Assert the function skips the user if the mentioned name is an empty string."""
        response = create_hello_response_based_on_time("")
        assert response == "Cześć!"

    def test_mentions_the_time_in_response(self):
        """Assert the response contains time corresponding to the passed enum."""
        response = create_hello_response_based_on_time(user_id=None, time=TimesOfDay.EVENING)
        assert response == "Dobry wieczór!"

    def test_mentions_both_user_and_time(self):
        """Assert that message is properly constructed when both user and time are mentioned."""
        name = "KochamMinecraft2137"
        time = TimesOfDay.NIGHT
        response = create_hello_response_based_on_time(name, time)
        assert response == f"*zieeew* No cześć, <@{name}>."


class TestTimeBasedGreeting:
    """Test suite for '_get_time_based_greeting()' helper function."""

    def test_no_time_given_raises_error(self):
        """Assert that the function always needs the time argument and will fail otherwise."""
        with pytest.raises(TypeError):
            _get_time_based_greeting()

    @pytest.mark.parametrize(
        ("time", "expected_response"),
        [
            (TimesOfDay.MORNING, "Witam w ten przepiękny poranek"),
            (TimesOfDay.AFTERNOON, "Dzień dobry"),
            (TimesOfDay.EVENING, "Dobry wieczór"),
            (TimesOfDay.NIGHT, "*zieeew* No cześć"),
        ],
    )
    def test_returns_matching_greeting(self, time, expected_response):
        """Assert that the function returns expected greeting based on the time input."""
        greeting = _get_time_based_greeting(time)
        assert greeting == expected_response

    def test_return_dummy_value_when_no_matching_case(self):
        """Assert the function returns a dummy value when the given enum doesn't match any case."""

        class FakeEnum(Enum):
            MISSING = "This value won't be found in the function's body"

        fake_enum = FakeEnum.MISSING

        missing_greeting = _get_time_based_greeting(fake_enum)
        assert missing_greeting == "Cześć"
