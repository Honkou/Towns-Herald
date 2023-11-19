"""Module that groups Discord commands.

Each class needs to be then imported to main.py as a cog.
"""
import discord
from discord.ext import commands


class Commands(commands.Cog):
    """Class for Discord commands.

    Each method should be named the same way as the respective command.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Commands class."""
        self.bot = bot

    @commands.command()
    async def hello(self, message: discord.message.Message) -> None:
        """Respond with greeting appropriate to bot's timezone."""
        await message.channel.send("Siema Eniu")
