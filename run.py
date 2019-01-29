from src import app

try:
	app.bot.run(app.env['token'], bot=True, reconnect=True)
except Exception as e:
	print(e)