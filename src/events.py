from .app import app 
import sys, traceback
from discord.ext import commands

class Events():
	@app.bot.event
	async def on_ready():
		print("Connected to Discord as {bot.user.name}".format(bot=app.bot))
	@app.bot.event
	async def on_command_error(ctx, error):
		if isinstance(error, commands.CommandNotFound):
			return
		try:
			await ctx.send(f"Error: {error}")
		except:
			pass
	@app.bot.event
	async def on_message(message):
		if message.author.bot:
			return
		await app.bot.process_commands(message)