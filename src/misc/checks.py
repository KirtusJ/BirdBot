import discord
from discord.ext import commands

from src.models import DiscordUser
from src.models.model import database
from .exceptions import NotOwner, NotModerator, Blacklisted

class Checks():
	def __init__(self):
		self.__initsets__()
	def __initsets__(self):
		self.owners = database.session.query(DiscordUser).filter_by(owner=True).all()
		self.moderators = database.session.query(DiscordUser).filter_by(moderator=True).all()
		self.blacklisted = database.session.query(DiscordUser).filter_by(blacklisted=True).all()
	def is_owner(self):
		async def predicate(ctx):
			user = database.session.query(DiscordUser).filter_by(id=ctx.author.id).first()
			if user.owner:
				return True
			else:
				raise NotModerator("You must be an owner to use this command")
		return commands.check(predicate)
	def is_mod(self):
		async def predicate(ctx):
			user = database.session.query(DiscordUser).filter_by(id=ctx.author.id).first()
			if user.moderator or user.owner:
				return True
			else:
				raise NotModerator("You must be a moderator to use this command")
		return commands.check(predicate)
	def not_blacklisted(self):
		async def predicate(ctx):
			user = database.session.query(DiscordUser).filter_by(id=ctx.author.id).first()
			if user.blacklisted:
				raise Blacklisted("You cannot use this command if you are blacklisted")
			else:
				return True
		return commands.check(predicate)

checks = Checks()