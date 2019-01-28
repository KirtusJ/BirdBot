import discord
from discord.ext import commands
from src.models import DiscordUser
from src.models.model import database
from src.misc import checks

class CogModule:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, hidden=True)
    @checks.is_owner()
    @checks.not_blacklisted()
    async def module(self, ctx):
        """ Module commands """

    @module.command(pass_context=True, hidden=True)
    async def load(self, ctx, *, cog: str):
        """Command which loads a Module."""
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"```py\nError {type(e).__name__} - {e}```")
        else:
            await ctx.send(f"```py\nSuccess: {cog} loaded```")


    @module.command(pass_context=True, hidden=True)
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module."""
        try: 
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f"```py\nError: {type(e).__name__} - {e}```")
        else:
            await ctx.send(f"```py\nSuccess: {cog} unloaded```")

    @module.command(pass_context=True, hidden=True)
    async def reload(self, ctx, *, cog: str):
        """Command which reloads a Module."""
        try: 
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"```py\nError: {type(e).__name__} - {e}```")
        else:
            await ctx.send(f"```py\nSuccess: {cog} reloaded```")
def setup(bot):
    bot.add_cog(CogModule(bot))
