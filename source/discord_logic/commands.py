"""Module that groups Discord commands.

Each class needs to be then imported to main.py as a cog.
"""
import server_time
from discord.ext import commands
from discord_logic.message_constructors import create_hello_response_based_on_time


class Commands(commands.Cog):
    """Class for Discord commands.

    Each method should be named the same way as the respective command.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Commands class."""
        self.bot = bot

    @commands.command()
    async def hello(self, context: commands.Context) -> None:
        """Respond with greeting appropriate to the bot's timezone.

        Example responses:
        "Dobry wieczór, honkou!" - sent in the evening if prompted by honkou
        "*zieeew* No cześć, Shiro." - sent in the night if prompted by Shiro
        """
        author_id = context.message.author.id
        part_of_the_day = server_time.get_servers_time_of_day()

        response = create_hello_response_based_on_time(author_id, part_of_the_day)
        await context.channel.send(response)
