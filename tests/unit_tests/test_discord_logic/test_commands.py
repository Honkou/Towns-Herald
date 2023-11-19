"""File for testing discord_logic.commands.py."""
import discord.ext.test as dpytest
import pytest


@pytest.mark.usefixtures("fake_bot")
@pytest.mark.asyncio()
async def test_hello():
    """Assert that sending !hello command returns expected greeting."""
    await dpytest.message("!hello")
    assert dpytest.verify().message().content("Siema Eniu")
