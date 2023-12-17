"""Module that groups Discord commands.

Each class needs to be then imported to main.py as a cog.
"""
from discord.ext import commands


class Commands(commands.Cog):
    """Class for Discord commands.

    Each method should be named the same way as the respective command.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Commands class."""
        self.bot = bot

    @commands.command()
    async def hello(self, context: commands.Context) -> None:
        """Respond with greeting appropriate to bot's timezone."""
        await context.channel.send("Siema Eniu")
