import discord
from discord.ext import commands
from src.models import DiscordUser
from src.models.model import database
from src.misc import checks

from datetime import datetime

class ModeratorModule:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.not_blacklisted()
    async def convert(self, ctx, *, temp):
        embed = discord.Embed(title="Conversion", description=conversionFormula(temp), color=0x4286f4)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def add_mod(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id).first()
        if user_filter:
            if not user_filter.moderator == True:
                if not user_filter.owner == True:
                    user_filter.moderator=True
                    user_filter.updated=datetime.now()
                    database.session.commit()
                    await ctx.send(f"{user.mention} is now a moderator!")
                else:
                    user_filter.moderator=True
                    user_filter.owner=False
                    user_filter.updated=datetime.now()
                    database.session.commit()
                    await ctx.send(f"{user.mention} is now a moderator!")
            else:
                await ctx.send(f"{user.mention} is already a moderator!")
        else:
            discord_user = DiscordUser(id=user.id, moderator=True)
            database.session.add(discord_user)
            database.session.commit()
            await ctx.send(f"{user.mention} is now a moderator!")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def remove_mod(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id).first()
        if user_filter:
            if user_filter.moderator == True:
                user_filter.moderator=False
                user_filter.updated=datetime.now()
                database.session.commit()
                await ctx.send(f"{user.mention} is no longer a moderator!")
            else:
                await ctx.send(f"{user.mention} isn't a moderator!")
        else:
            await ctx.send(f"{user.mention} isn't a moderator!")


    @commands.command(pass_context=True)
    @checks.is_owner()
    async def add_owner(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id).first()
        if user_filter:
            if not user_filter.owner == True:
                if not user_filter.moderator == True:
                    user_filter.owner=True
                    user_filter.updated=datetime.now()
                    database.session.commit()
                    await ctx.send(f"{user.mention} is now an owner!")
                else:
                    user_filter.moderator=False
                    user_filter.owner=True
                    user_filter.updated=datetime.now()
                    database.session.commit()
                    await ctx.send(f"{user.mention} is now an owner!")
            else:
                await ctx.send(f"{user.mention} is already an owner!")
        else:
            discord_user = DiscordUser(id=user.id, owner=True)
            database.session.add(discord_user)
            database.session.commit()
            await ctx.send(f"{user.mention} is now an owner!")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def remove_owner(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id).first()
        if user_filter:
            if user_filter.owner == True:
                user_filter.owner=False
                user_filter.updated=datetime.now()
                database.session.commit()
                await ctx.send(f"{user.mention} is no longer an owner!")
            else:
                await ctx.send(f"{user.mention} isn't an owner!")
        else:
            await ctx.send(f"{user.mention} isn't an owner!")

    @commands.command(pass_context=True)
    @checks.is_mod()
    async def blacklist(self, ctx, user: discord.Member):
        user_filter = database.session.query(DiscordUser).filter_by(id=user.id).first()
        if user_filter:
            if not user_filter.blacklisted == True:
                user_filter.blacklisted=True
                user_filter.updated=datetime.now()
                database.session.commit()
                await ctx.send(f"{user.mention} is now blacklisted!")
            else:
                user_filter.blacklisted=False
                user_filter.updated=datetime.now()
                database.session.commit()
                await ctx.send(f"{user.mention} is no longer blacklisted!")
        else:
            discord_user = DiscordUser(id=user.id, blacklisted=True)
            database.session.add(discord_user)
            database.session.commit()
            await ctx.send(f"{user.mention} is now blacklisted!")

    @commands.command(pass_context=True)
    async def mods(self, ctx):
        """shows a list of mods or some shit idiot"""
        mods = database.session.query(DiscordUser).filter_by(moderator=True).all()
        if mods:
            embed = discord.Embed(title="Moderators", description="List of bot mods", color=0x4286f4)
            for mod in mods:
                embed.add_field(name="\u200b", value=f"<@{mod.id}>", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("There are no mods")
    @commands.command(pass_context=True)
    async def owners(self, ctx):
        owners = database.session.query(DiscordUser).filter_by(owner=True).all()
        if owners:
            embed = discord.Embed(title="Owners", description="List of bot owners", color=0x4286f4)
            for owner in owners:
                embed.add_field(name="\u200b", value=f"<@{owner.id}>", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("There are no owners")

    @commands.command(pass_context=True)
    async def blacklisted(self, ctx):
        blacklisted = database.session.query(DiscordUser).filter_by(blacklisted=True).all()
        if blacklisted:
            embed = discord.Embed(title="Blacklisted", description="List of blacklisted users", color=0x4286f4)
            for user in blacklisted:
                embed.add_field(name="\u200b", value=f"<@{user.id}>", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("There are no blacklisted users")

def setup(bot):
    bot.add_cog(ModeratorModule(bot))

def conversionFormula(inp):
    try:
        if not '°' in inp:
            degree = float(inp[:-1]) 
        else:
            degree = float(inp[:-2])
    except Exception as e:
        return e
    opt = ['c','C','f','F'] 
    if inp.endswith(opt[0]) or inp.endswith(opt[1]):
        return f"{round(float(9 * degree / 5 + 32),2)}°F"
    elif inp.endswith(opt[2]) or inp.endswith(opt[3]):
        return f"{round(float((degree - 32) * 5 / 9),2)}°C"
    return "Invalid input"