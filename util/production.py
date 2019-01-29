import json

with open("util/database/database.json", "r") as db:
	data = json.load(db)
	db_production = data["production"]

with open("util/bot/secret.json", "r") as bot:
	data = json.load(bot)
	bot_production = data["production"]

db_production = {
	"username" : db_production["username"],
	"password" : db_production["password"],
	"host" : db_production["host"],
	"name" : db_production["name"],
	"link" : "{manager}://{username}:{password}@{host}/{name}?charset=utf8mb4".format(
				manager=db_production["manager"], username=db_production["username"], 
				password=db_production["password"], host=db_production["host"], name=db_production["name"]
			)
}

bot_production = {
	"mode" : bot_production["mode"],
	"token" : bot_production["token"],
	"secret" : bot_production["secret"]
}


