"""File for testing discord_logic.events.py."""
import discord.ext.test as dpytest
import pytest


@pytest.mark.usefixtures("fake_bot")
@pytest.mark.asyncio()
async def test_marco():
    """Assert that sending 'Marco' returns 'Polo!'."""
    await dpytest.message("Marco")
    assert dpytest.verify().message().content("Polo!")
