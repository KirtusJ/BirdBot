import json

with open("util/database/database.json", "r") as db:
	data = json.load(db)
	db_development = data['development']

with open("util/bot/secret.json", "r") as bot:
	data = json.load(bot)
	bot_development = data["development"]

db_development = {
	"username" : db_development["username"],
	"password" : db_development["password"],
	"host" : db_development["host"],
	"name" : db_development["name"],
	"link" : "{manager}://{username}:{password}@{host}/{name}?charset=utf8mb4".format(
				manager=db_development["manager"], username=db_development["username"], 
				password=db_development["password"], host=db_development["host"], name=db_development["name"]
			)
}

bot_development = {
	"mode" : bot_development["mode"],
	"token" : bot_development["token"],
	"secret" : bot_development["secret"]
}

