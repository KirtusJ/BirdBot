from discord.ext import commands

class NotOwner(commands.CheckFailure):
	pass
class NotModerator(commands.CheckFailure):
	pass
class Blacklisted(commands.CheckFailure):
	pass