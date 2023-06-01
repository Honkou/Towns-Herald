"""File containing all unit tests for main.py file."""
import pytest
from main import get_token


class TestGetToken:
    """A class for all get_token related tests."""

    def test_get_proper_token(self, set_environment_variable) -> None:
        """Check if get_token properly returns the token from environment."""
        assert get_token() == "Test_string"

    def test_error_when_token_missing(self) -> None:
        """Check if the function properly raises KeyError when
        there is no DISCORD_TOKEN key in the environment.
        """
        with pytest.raises(KeyError):
            get_token()
