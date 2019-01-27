import os 

from .bot.bot import bot as bot_config
from .bot.development import development as bot_development
from .bot.production import production as bot_production

from .database.development import development as db_development
from .database.production import production as db_production

def bot_env():
	try:
		env = os.environ['BOT_ENV']
	except:
		env = None
	if env:
		if "development" in env.lower():
			BOT_ENV = bot_development
		elif "production" in env.lower():
			BOT_ENV = bot_production
		else:
			BOT_ENV = bot_development
	else:
		BOT_ENV = bot_development
	return BOT_ENV

def database(env):
	if env["mode"] == "production":
		return db_production
	elif env["mode"] == "development":
		return db_development