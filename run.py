from src import app

app.bot.run(app.env['token'], bot=True, reconnect=True)