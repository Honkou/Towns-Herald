"""Configuration file for pytest."""
import os

import discord
import discord.ext.test as dpytest
import pytest
import pytest_asyncio
from discord.ext import commands
from discord_logic.events import Listeners


@pytest.fixture()
def _set_environment_variable() -> None:
    """Create a token environment variable for testing.

    After the test is finished (pass or fail), delete the variable.
    """
    os.environ["DISCORD_TOKEN"] = "Test_token"

    yield

    os.environ.pop("DISCORD_TOKEN")


@pytest_asyncio.fixture()
async def fake_bot() -> commands.Bot:
    """Create a fake bot for command testing."""
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    await bot._async_setup_hook()  # noqa: SLF001 (ignore accessing private method)
    await bot.add_cog(Listeners(bot))
    dpytest.configure(bot)

    yield bot

    await dpytest.empty_queue()
