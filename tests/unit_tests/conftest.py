"""Configuration file for pytest."""
import os

import discord
import discord.ext.commands as commands
import discord.ext.test as dpytest
import pytest
import pytest_asyncio
from handle_messages import Listeners


@pytest.fixture()
def set_environment_variable():
    """Create a token environment variable for testing.

    After the test is finished (pass or fail), delete the variable.
    """
    os.environ["DISCORD_TOKEN"] = "Test_token"

    yield

    os.environ.pop("DISCORD_TOKEN")


@pytest_asyncio.fixture()
async def fake_bot():
    """Create a fake bot for command testing."""
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    await bot._async_setup_hook()
    await bot.add_cog(Listeners(bot))
    dpytest.configure(bot)

    yield bot

    await dpytest.empty_queue()
