from util import bot_env, bot_config
from discord.ext import commands
import sys, traceback
from .database import database

class Application():
	def __init__(self, env, bot_config):
		print("Initializing Application in {env} mode".format(env=env['mode']))
		self.__config__(env, bot_config)
		database.__initdb__(self.env)
		self.__create__()
		self.load_extensions()
	def __config__(self, env, config):
		self.env = env
		self.name = bot_config['name']
		self.description = bot_config['description']
		self.version = bot_config['version']
		self.prefixes = bot_config['prefixes']
		self.extensions = bot_config['extensions']
		self.owners = bot_config['owners']

	def __create__(self):
		self.bot = commands.Bot(command_prefix=self.prefixes, description=self.description)
	def load_extensions(self):
		for extension in self.extensions:
			try:
				self.bot.load_extension(extension)
			except Exception as e:
				print(f'Failed to load extension {extension}.', file=sys.stderr)
				traceback.print_exc()		

app = Application(bot_env(), bot_config)
