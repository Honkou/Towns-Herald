"""Module that handles user messages.

Should contain separate classes for regular messages and commands.
Each class needs to be then imported to main.py as a cog.
"""
import discord
from discord.ext import commands


class Listeners(commands.Cog):
    """Class for regular messages."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Listeners class."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message) -> None:
        """Listen to messages sent to chat."""
        if message.author.bot:
            return

        if message.content.startswith("Marco"):
            await message.channel.send("Polo!")

        if message.content == "Polo!":
            await message.channel.send("Cockta!")
