import json

with open("util/bot/bot.json", "r") as bot:
	data = json.load(bot)
	production = data["production"]

production = {
	"mode" : "production",
	"token" : production["token"],
	"secret" : production["secret"]
}


