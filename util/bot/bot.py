import json

with open("util/bot/bot.json", "r") as bot:
	data = json.load(bot)
	app = data["bot"]

bot = {
	"name" : app["name"],
	"description" : app["description"],
	"version" : app["version"],
	"prefixes" : app["prefixes"],
	"extensions" : app["extensions"]
}