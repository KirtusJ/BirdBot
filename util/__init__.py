import os 

from .public import bot_config
from .development import bot_development, db_development
from .production import bot_production, db_production

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