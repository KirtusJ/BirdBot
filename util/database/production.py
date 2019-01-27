import json

with open("util/database/database.json", "r") as db:
	data = json.load(db)
	production = data["development"]

production = {
	"username" : production["username"],
	"password" : production["password"],
	"host" : production["host"],
	"name" : production["name"],
	"link" : "mysql://{username}:{password}@{host}/{name}?charset=utf8mb4".format(
				username=production["username"], password=production["password"],
				host=production["host"], name=production["name"]
			)
}
