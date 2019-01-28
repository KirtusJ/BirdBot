from .app import app 
from .database import database
from src.models.discord_users import DiscordUser
import sys, traceback
from discord.ext import commands

from src.misc.exceptions import NotModerator, NotOwner, Blacklisted

class Events():
	@app.bot.event
	async def on_ready():
		print("Connected to Discord as {bot.user.name}".format(bot=app.bot))
		for owner_id in app.owners:
			owner = database.session.query(DiscordUser).filter_by(id=owner_id).first()
			if not owner:
				new_owner = DiscordUser(id=owner_id, owner=True)
				database.session.add(new_owner)
				database.session.commit()
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