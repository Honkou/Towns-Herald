"""Configuration file for pytest."""
import os

import pytest


@pytest.fixture()
def set_environment_variable():
    """Create a token environment variable for testing.

    After the test is finished (pass or fail), delete the variable.
    """
    os.environ["DISCORD_TOKEN"] = "Test_string"
    yield
    os.environ.pop("DISCORD_TOKEN")
