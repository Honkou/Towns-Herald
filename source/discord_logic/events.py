"""Module that handles Discord events.

Each class needs to be then imported to main.py as a cog.
"""
import discord
from discord.ext import commands


class Listeners(commands.Cog):
    """Class for regular messages.

    Should contain separate methods for each event the bot is supposed to react to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Listeners class."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message) -> None:
        """Listen and react to regular messages sent to chat."""
        if message.author.bot:
            return

        if message.content.startswith("Marco"):
            await message.channel.send("Polo!")

        if message.content == "Polo!":
            await message.channel.send("Cockta!")
