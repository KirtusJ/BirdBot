import discord
from discord.ext import commands

from src.models import DiscordUser
from src.models.model import database

class Checks():
	def __init__(self):
		self.__initsets__()
	def __initsets__(self):
		self.owners = database.session.query(DiscordUser).filter_by(role="owner").all()
		self.moderators = database.session.query(DiscordUser).filter_by(role="moderator").all()
	def is_owner(self):
		async def predicate(ctx):
			for owner in self.owners:
				if ctx.author.id == owner.id:
					return True
				else:
					return False
		return commands.check(predicate)
	def is_mod(self):
		async def predicate(ctx):
			for mod in self.moderators:
				if ctx.author.id == mod.id:
					return True
				else:
					return False
		return commands.check(predicate)

checks = Checks()