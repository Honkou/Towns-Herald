"""Main file to run. It should gather all logic and run as one thread."""
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from handle_messages import Listeners


def get_token() -> str:
    """Find and return proper Discord authorization token."""
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise KeyError("Not able to find Discord credentials")
    return token


def run_service() -> None:
    """Prepare and run main bot thread."""
    load_dotenv()
    discord_token = get_token()

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def setup_hook() -> None:
        """On start, add all bot commands as cogs.

        Documentation on cogs available here:
        https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#quick-example
        """
        await bot.add_cog(Listeners(bot))

    bot.run(discord_token)


if __name__ == "__main__":
    run_service()
