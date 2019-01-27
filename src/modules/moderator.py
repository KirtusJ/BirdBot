import discord
from discord.ext import commands

from src.models import DiscordUser
from src.models.model import database

from src.misc import checks

class ModeratorModule:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def add_mod(self, ctx, user: discord.Member):
        if not database.session.query(DiscordUser).filter_by(id=user.id, role="moderator").first():
            if not database.session.query(DiscordUser).filter_by(id=user.id, role="owner").first():
                discord_user = DiscordUser(id=user.id, role="moderator")
                database.session.add(discord_user)
                database.session.commit()
                await ctx.send(f"{user.mention} is now a moderator!")
            else:
                await ctx.send(f"{user.mention} is an owner!")
        else:
            await ctx.send(f"{user.mention} is already a moderator!")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def remove_mod(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id, role="moderator").first()
        if user_filter:
            database.session.delete(user_filter)
            database.session.commit()
            await ctx.send(f"{user.mention} is no longer a moderator!")
        else:
            await ctx.send(f"{user.mention} isn't a moderator!")


    @commands.command(pass_context=True)
    @checks.is_owner()
    async def add_owner(self, ctx, user: discord.Member):
        if not database.session.query(DiscordUser).filter_by(id=user.id, role="owner").first():
            if not database.session.query(DiscordUser).filter_by(id=user.id, role="moderator").first():
                discord_user = DiscordUser(id=user.id, role="owner")
                database.session.add(discord_user)
                database.session.commit()
                await ctx.send(f"{user.mention} is now a owner!")
            else:
                await ctx.send(f"{user.mention} is a moderator!")
        else:
            await ctx.send(f"{user.mention} is already a owner!")
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def remove_owner(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id, role="owner").first()
        if user_filter:
            database.session.delete(user_filter)
            database.session.commit()
            await ctx.send(f"{user.mention} is no longer an owner!")
        else:
            await ctx.send(f"{user.mention} isn't an owner!")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def mods(self, ctx):
        mods = database.session.query(DiscordUser).filter_by(role="moderator").all()
        if mods:
            for mod in mods:
                await ctx.send(f"<@{mod.id}>")
        else:
            await ctx.send("There are no mods")
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def owners(self, ctx):
        owners = database.session.query(DiscordUser).filter_by(role="owner").all()
        if owners:
            for owner in owners:
                await ctx.send(f"<@{owner.id}>")
        else:
            await ctx.send("There are no owners")

def setup(bot):
    bot.add_cog(ModeratorModule(bot))