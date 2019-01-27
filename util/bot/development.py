import json

with open("util/bot/bot.json", "r") as bot:
	data = json.load(bot)
	development = data["development"]

development = {
	"mode" : "development",
	"token" : development["token"],
	"secret" : development["secret"]
}

