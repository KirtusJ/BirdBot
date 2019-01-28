import discord
from discord.ext import commands
from src.models import DiscordUser
from src.models.model import database
from src.misc import checks
from src.misc.func.conversion import conversion

class MiscModule:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.not_blacklisted()
    async def convert(self, ctx, *, temp):
        embed = discord.Embed(title="Conversion", description=conversion(temp), color=0x4286f4)
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    @checks.not_blacklisted()
    async def say(self, ctx, *, input):
        await ctx.send(input)

    @commands.command(pass_context=True)
    @checks.not_blacklisted()
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping", description="{0}ms".format(int(self.bot.latency * 1000)), color=0x4286f4)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(MiscModule(bot))
