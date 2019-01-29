import discord
from discord.ext import commands
from src.models import DiscordUser
from src.models.model import database
from src.misc import checks
from src.misc.func.conversion import conversion

from util import bot_config

class UtilityModule:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):
        """ Shows bot info """
        # obviously more stuff will be put here
        embed = discord.Embed(title=bot_config['name'], description=bot_config['description'], color=0X008CFF)
        embed.add_field(name="Invite", value=f"https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=0&scope=bot", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UtilityModule(bot))