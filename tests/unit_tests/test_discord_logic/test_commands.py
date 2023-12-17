"""File for testing discord_logic.commands.py."""
from unittest.mock import patch

import discord.ext.test as dpytest
import pytest
from server_time import TimesOfDay


@pytest.mark.usefixtures("fake_bot")
@pytest.mark.asyncio()
async def test_hello_in_the_morning():
    """Assert that sending !hello command in the morning returns expected greeting.

    The assertion needs to be partial, as the dpytest always generates different user_id.
    """
    with patch("server_time.get_servers_time_of_day", autospec=True, return_value=TimesOfDay.MORNING):
        await dpytest.message("!hello")
    response = dpytest.get_message(peek=True)

    assert (
        dpytest.verify().message().contains().content("Witam w ten przepiękny poranek, <@")
    ), response.content
