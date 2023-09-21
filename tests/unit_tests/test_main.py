"""File containing all unit tests for main.py file."""
import pytest
from main import get_token, run_service
from pytest_mock import MockerFixture


class TestGetToken:
    """A class for all get_token related tests."""

    @pytest.mark.usefixtures("_set_environment_variable")
    def test_get_proper_token(self) -> None:
        """Check if get_token properly returns the token from environment."""
        assert get_token() == "Test_token"

    def test_error_when_token_missing(self) -> None:
        """Check if the function properly raises KeyError without the proper token."""
        with pytest.raises(KeyError):
            get_token()


@pytest.mark.usefixtures("_set_environment_variable")
def test_run_service(mocker: MockerFixture) -> None:
    """Assert that bot.run is being properly called.

    To achieve that, make the load_dotenv() function and
    Bot.run() method do nothing.
    We only need to assert that the function is called and it uses the token
    parsed with set_environment_variable fixture.
    """
    mocker.patch("main.load_dotenv")
    stubbed_bot = mocker.patch("main.commands.Bot.run")
    run_service()
    stubbed_bot.assert_called_once_with("Test_token")
