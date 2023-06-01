"""File for testing handle_messages.py."""
import discord.ext.test as dpytest
import pytest


@pytest.mark.asyncio
async def test_marco(fake_bot):
    """Assert that sending Marco returns Polo!"""
    await dpytest.message("Marco")
    assert dpytest.verify().message().content("Polo!")
