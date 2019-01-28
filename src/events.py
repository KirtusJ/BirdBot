from .app import app 
import sys, traceback
from discord.ext import commands

from src.misc.exceptions import NotModerator, NotOwner, Blacklisted

class Events():
	@app.bot.event
	async def on_ready():
		print("Connected to Discord as {bot.user.name}".format(bot=app.bot))
	@app.bot.event
	async def on_command_error(ctx, error):
		e_fmt = f"```{error}```"
		if isinstance(error, commands.CommandNotFound):
			return
		if isinstance(error, NotModerator):
			await ctx.send(e_fmt)
			return
		if isinstance(error, NotOwner):
			await ctx.send(e_fmt)
			return
		if isinstance(error, Blacklisted):
			await ctx.send(e_fmt)
			return
		try:
			await ctx.send(e_fmt)
		except:
			pass
	@app.bot.event
	async def on_message(message):
		if message.author.bot:
			return
		await app.bot.process_commands(message)