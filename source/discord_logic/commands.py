"""Module that groups Discord commands.

Each class needs to be then imported to main.py as a cog.
"""
from discord.ext import commands
from discord_logic.message_constructors import create_hello_response_based_on_time
from server_time import get_servers_time_of_day


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
        author = context.message.author.display_name
        part_of_the_day = get_servers_time_of_day()
        response = create_hello_response_based_on_time(author, part_of_the_day)
        await context.channel.send(response)
