import json

with open("util/bot/public.json", "r") as bot:
	data = json.load(bot)
	app = data["bot"]

bot_config = {
	"name" : app["name"],
	"description" : app["description"],
	"version" : app["version"],
	"prefixes" : app["prefixes"],
	"extensions" : app["extensions"],
	"owners" : app["owners"]
}